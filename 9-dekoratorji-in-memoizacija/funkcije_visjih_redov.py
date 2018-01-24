# =============================================================================
# Funkcije višjih redov
#
# Spodaj je primer funkcije višjega reda `eksponentna(a)`, ki kot argument
# dobi število $a$ in vrne funkcijo $x \mapsto a^x$. Zgled uporabe:
# 
#     >>> f = eksponentna(2)
#     >>> f(5)
#     32
#     >>> f(0.5)
#     1.4142135623730951
# =====================================================================@011780=
# 1. podnaloga
# Sestavite funkcijo `linearna(a, b)`, ki kot argumenta dobi števili $a$
# in $b$ ter vrne funkcijo $x \mapsto a \cdot x + b$. Zgled:
# 
#     >>> f = linearna(3, 2)
#     >>> f(0.5)
#     3.5
# =============================================================================
import math

def eksponentna(a):
    return (lambda x: a ** x)

def linearna(a, b):
    return (lambda x: a * x + b)
# =====================================================================@011781=
# 2. podnaloga
# Sestavite funkcijo `kompozitum(f, g)`, ki kot argumenta dobi funkciji
# `f` in `g`, ter vrne njun kompozitum.
# Zgled:
# 
#     >>> import math
#     >>> f = kompozitum(abs, math.sin)
#     >>> f(3*math.pi/2)
#     1.0
# =============================================================================
def kompozitum(f, g):
    '''Vrne kompozitum funkcij.'''
    return (lambda x: f(g(x)))
# =====================================================================@011782=
# 3. podnaloga
# Sestavite funkcijo `odvod(f, epsilon=10e-5)`, ki sprejme funkcijo `f`
# in vrne njen odvod (ki je spet funkcija). Odvod v točki `x` ocenimo z izrazom
# $f'(x) \approx (f(x + \epsilon/2) - f(x - \epsilon/2)) / \epsilon$.
# Zgled:
# 
#     >>> f = odvod((lambda x: x * x + 1))
#     >>> f(1.0)
#     2.000000000002
# =============================================================================
def odvod(f, epsilon=10**-5):
    return (lambda x: (f(x + epsilon/2) - f(x - epsilon/2)) / epsilon)
# =====================================================================@011783=
# 4. podnaloga
# Sestavite funkcijo `uporabi_nkrat(f, x, n)`, ki kot argumente dobi
# funkcijo `f`, število `x` in naravno število `n` ter vrne število, ki
# ga dobimo, če na `x` funkcijo `f` uporabimo $n$-krat. Zgled:
# 
#     >>> collatz = lambda x: x // 2 if x % 2 == 0 else 3*x + 1
#     >>> uporabi_nkrat(collatz, 13, 7)
#     4
# =============================================================================
def uporabi_nkrat(f, x, n):
    '''Vrne število, ki ga dobimo, če n krat kličemo f na x.'''
    for _ in range(n):
        x = f(x)
    return x
# =====================================================================@011784=
# 5. podnaloga
# Sestavite funkcijo `uporabi_vse(sez, x)`, ki kot argumenta dobi seznama
# funkcij `sez` in število `x`. Funkcija naj vsako od funkcij iz `sez` uporabi
# na `x` in vrne seznam tako dobljenih števil. Zgled:
# 
#     >>> f = lambda x: x**2 - 3*x + 4
#     >>> g = lambda x: x**x
#     >>> uporabi_vse([math.sin, math.cos, f, g, abs, int], math.pi/2)
#     [1.0, 6.123233995736766e-17, 1.7550121198876498, 2.032658322210728, 1.5707963267948966, 1]
# =============================================================================
def uporabi_vse(sez, x):
    '''Na x uporabi vse funkcije iz seznama.'''
    sezStevil = []
    for f in sez:
        sezStevil.append(f(x))
    return sezStevil


def sestej():
    return lambda a, b: a + b

print(sestej()(2, 5))




































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import io, json, os, re, sys, shutil, traceback, urllib.error, urllib.request


from contextlib import contextmanager

class Check:
    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []
        Check.current_part = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = clean or Check.clean
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env={}):
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        actual_result = eval(expression, globals(), local_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def run(statements, expected_state, clean=None, env={}):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        s = {}
        s.update(env)
        clean = clean or Check.clean
        exec(code, globals(), s)
        errors = []
        for (x, v) in expected_state.items():
            if x not in s:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(s[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, s[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, encoding=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        sys.stdin = io.StringIO('\n'.join(content))
        try:
            yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, use_globals=False):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            def visible_input(prompt):
                inp = input(prompt)
                print(inp)
                return inp
            exec(expression, globals() if use_globals else {'input': visible_input})
        finally:
            output = sys.stdout.getvalue().strip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['je enaka'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def generator(expression, expected_values, should_stop=False, further_iter=0, env={}, clean=None):
        from types import GeneratorType
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        gen = eval(expression, globals(), local_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(further_iter):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if should_stop:
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\n'  # beginning of header
            r'(#( [^\n]*)?\n)+'       # description
            r'# =+\n'                 # end of header
            r'(?P<solution>.*?)'      # solution
            r'(?=\n# =+@)',           # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        
        try:
            test_data = [
                (["f = linearna(3, 2)", "y = f(0.5)"], {'y': 3.5}),
                (["f = linearna(3, 2)", "y = f(2.5)"], {'y': 9.5}),
                (["f = linearna(3, 2)", "y = f(-3)"], {'y': -7}),
                (["f = linearna(-3, 2.5)", "y = f(0.5)"], {'y': 1}),
                (["f = linearna(0, 7.3)", "y = f(1)"], {'y': 7.3}),
                (["f = linearna(7, -9)", "y = f(2)"], {'y': 5}),
                (["f = linearna(1.5, -5)", "y = f(-9)"], {'y': -18.5}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            import math
            test_data = [
                (["f = lambda x: x**2", "g = lambda x: x**2 + 3*x + 4",
                  "h = kompozitum(f, g)", "x = h(2)"], {'x': 196}),
                (["f = lambda x: x**2", "g = lambda x: x**2 + 3*x + 4",
                  "h = kompozitum(f, g)", "x = h(-1)"], {'x': 4}),
                (["f = lambda x: x**2", "g = lambda x: x**2 + 3*x + 4",
                  "h = kompozitum(g, f)", "x = h(2)"], {'x': 32}),
                (["f = lambda x: x**2", "g = lambda x: x**2 + 3*x + 4",
                  "h = kompozitum(g, f)", "x = h(-1)"], {'x': 8}),
                (["h = kompozitum(math.sin, math.log)", "x = h(3)"], {'x': 0.8905770416677471}),
                (["h = kompozitum(math.sin, math.log)", "x = h(2)"], {'x': 0.6389612763136348}),    
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            import math
            
            Check.equal("odvod((lambda x: x))(1.0)", 1.0)
            Check.equal("odvod((lambda x: x * x))(0.0)", 0.0)
            Check.equal("odvod((lambda x: x * x))(1.0)", 2.0)
            Check.equal("odvod((lambda x: x * x))(3.0)", 6.0)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                (["collatz = lambda x: x // 2 if x % 2 == 0 else 3*x + 1",
                  "x = uporabi_nkrat(collatz, 13, 7)"], {'x': 4}),
                (["collatz = lambda x: x // 2 if x % 2 == 0 else 3*x + 1",
                  "x = uporabi_nkrat(collatz, 113, 7)"], {'x': 32}),
                (["f = lambda x: x**2 - 3*x + 2",
                  "x = uporabi_nkrat(f, 0.5, 17)"], {'x': 0.2314887767729059}),
                (["f = lambda x: x**2",
                  "x = uporabi_nkrat(f, 1.01, 12)"], {'x': 5.0158785658510925e+17}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                (["f = lambda x: x**2 - 3*x + 4",
                  "g = lambda x: x**x",
                  "l = uporabi_vse([math.sin, math.cos, f, g, abs, int], math.pi/2)"],
                {'l': [1.0, 6.123233995736766e-17, 1.7550121198876498, 2.032658322210728, 1.5707963267948966, 1]}),
                (["f = lambda x: x**2 - 3*x + 4",
                  "g = lambda x: x**x",
                  "l = uporabi_vse([math.sin, math.cos, f, g, abs, int], math.e)"],
                {'l': [0.41078129050290885, -0.9117339147869651, 3.234210613553514, 15.154262241479259, 2.718281828459045, 2]}),
                (["f = lambda x: x**2 + 3*x + 4",
                  "g = lambda x: math.log(x**2 + 1)",
                  "l = uporabi_vse([str, math.sin, math.tan, f, g, abs, round], math.pi/2)"],
                {'l': ['1.5707963267948966', 1.0, 1.633123935319537e+16, 11.179790080657028, 1.2434053508887264, 1.5707963267948966, 2]}),
                (["f = lambda x: x**2 + 3*x + 4",
                  "g = lambda x: math.log(x**2 + 1)",
                  "l = uporabi_vse([str, math.sin, math.tan, f, g, abs, round], -1)"],
                {'l': ['-1', -0.8414709848078965, -1.5574077246549023, 2, 0.6931471805599453, 1, -1]}),
            ]
            for td in test_data:
                if not Check.run(*td, clean=lambda l: [round(x, 9) if type(x) is float else x for x in l]):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token a7d3422f9635f98a67f097384251c60b342d336e'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print("Posodabljam datoteko... ", end="")
            backup_filename = backup(filename)
            r = urlopen(response['update'])
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(r.read().decode('utf-8'))
            print("Stara datoteka je preimenovana v {0}.".format(os.path.basename(backup_filename)))
            print("Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.")
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
