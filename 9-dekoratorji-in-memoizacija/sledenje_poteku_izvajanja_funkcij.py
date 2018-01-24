# =============================================================================
# Sledenje poteku izvajanja funkcij
# =====================================================================@011777=
# 1. podnaloga
# Sestavite funkcijo `izpisi_rezultat(f)`, ki sprejme funkcijo enega argumenta
# `f` in vrne funkcijo, ki pri danem argumentu `x` vrne isti rezultat, vendar
# prej še izpiše vrednost argumenta in rezultata. Na primer:
# 
#     >>> def g(x): return x + 2
#     >>> glasni_g = izpisi_rezultat(g)
#     >>> 10 * g(5)
#     70
#     >>> 10 * glasni_g(5)
#     Pri argumentu 5 je rezultat 7
#     70
# 
# Če ob definiciji funkcije `f` uporabite dekorator `@izpisi_rezultat`, bo `f`
# definirana kot `izpisi_rezultat(osnovni_f)`, kjer je `osnovni_f` funkcija,
# kakršna bi bila `f`, če ne bi uporabili dekoratorja. Na primer, če definirate:
# 
#     @izpisi_rezultat
#     def fakulteta(n):
#         if n == 0:
#             return 1
#         else:
#             return n * fakulteta(n - 1)
# 
# Bo klic funkcije `fakulteta` izpisoval svoj rezultat:
# 
#     >>> fakulteta(5)
#     Pri argumentu 0 je rezultat 1
#     Pri argumentu 1 je rezultat 1
#     Pri argumentu 2 je rezultat 2
#     Pri argumentu 3 je rezultat 6
#     Pri argumentu 4 je rezultat 24
#     Pri argumentu 5 je rezultat 120
#     120
# =============================================================================
def izpisi_rezultat(osnovni_f):
    '''Sproti izpisuje rezultat.'''
    def glasni_f(x):
        rezultat = osnovni_f(x)
        print('Pri argumentu {} je rezultat {}'.format(x, rezultat))
        return rezultat
    return glasni_f

@izpisi_rezultat
def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

izpisi_rezultat(fakulteta(5))
# =====================================================================@011778=
# 2. podnaloga
# Sestavite funkcijo `prikazi_izracune(f)`, ki sprejme funkcijo `f` poljubnega
# števila argumentov (pomagajte si z `*args`) in vrne funkcijo, ki pri danih
# argumentih vrne isti rezultat, vendar na začetku izračuna pove, kaj računa,
# na koncu pa izpiše opravljen izračun. Na primer, ob definiciji:
# 
#     @prikazi_izracune
#     def gcd(m, n):
#         if n == 0:
#             return m
#         else:
#             return gcd(n, m % n)
# 
# bo klic funkcije `gcd` izpisoval, kako poteka izračun:
# 
#     >>> gcd(123, 45)
#     gcd(123, 45) = ...
#     gcd(45, 33) = ...
#     gcd(33, 12) = ...
#     gcd(12, 9) = ...
#     gcd(9, 3) = ...
#     gcd(3, 0) = ...
#     gcd(3, 0) = 3
#     gcd(9, 3) = 3
#     gcd(12, 9) = 3
#     gcd(33, 12) = 3
#     gcd(45, 33) = 3
#     gcd(123, 45) = 3
#     3
# 
# Namig: do imena funkcije dostopate z `f.__name__`
# =============================================================================
def prikazi_izracune(osnovni_f):
    '''Dekorator za prikaz računov.'''
    def prikaz(*args):
        argumenti = ', '.join(list(map(str, args)))
        print('{}({}) = {}'.format(osnovni_f.__name__, argumenti, '...'))
        rezultat = osnovni_f(*args)
        print('{}({}) = {}'.format(osnovni_f.__name__, argumenti, rezultat))
        return rezultat
    return prikaz

@prikazi_izracune
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

gcd(123, 45)

# =====================================================================@011779=
# 3. podnaloga
# Sestavite funkcijo `prikazi_izvajanje(f)`, ki deluje tako kot
# `prikazi_izracune`, le da zaradi lepšega pregleda nad izvajanjem v vsakem
# klicu funkcije bolj zamakne izpis izračunov. Na primer, če definirate:
# 
#     @prikazi_izracun
#     def fib(n):
#         if n == 0 or n == 1:
#             return n
#         else:
#             return fib(n - 1) + fib(n - 2)
# 
# Bo klic funkcije `fib` izpisoval:
# 
#     >>> fib(3)
#     fib(3) = ...
#       fib(2) = ...
#         fib(1) = ...
#         fib(1) = 1
#         fib(0) = ...
#         fib(0) = 0
#       fib(2) = 1
#       fib(1) = ...
#       fib(1) = 1
#     fib(3) = 2
#     2
# =============================================================================
globina = 0
RAZMIK = '   '


def prikazi_izracune(f):
    def zamaknjena(x):
        global globina
        print(RAZMIK * globina, end='')
        print('{0}({1}) = {2}'.format(f.__name__, x, '...'))
        globina += 1
        rezultat = f(x)
        globina -= 1
        print(RAZMIK * globina, end='')
        print('{0}({1}) = {2}'.format(f.__name__, x, rezultat))

        return rezultat
    return zamaknjena

@prikazi_izracune
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

fib(3)



ze_izracunani = {}
def pametni_fib(n):
    if n not in ze_izracunani:
        vrednost = n if n < 2 else pametni_fib(n - 1) + pametni_fib(n - 2)
        ze_izracunani[n] = vrednost
    return ze_izracunani[n]

print(pametni_fib(40))

# Raje naredimo dekorator

def naredi_bolj_pametno(neumna_f):
    ze_izracunani = {} # Slovar z rezultati, ki ustrezajo parametrom
    def pametna_f(x):  # Pametna funkcija gleda v slovar
        if x not in ze_izracunani:
            vrednost = neumna_f(x)
            ze_izracunani[x] = vrednost
        return ze_izracunani[x]
    return pametna_f

@naredi_bolj_pametno
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(400))


from functools import lru_cache

@lru_cache(maxsize=200)
def fib2(n):
    return n if n < 2 else fib2(n - 1) + fib2(n - 2)

print(fib2(320))




































































































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
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNzc3fQ:1eeU6f:HffGUpZcEB9RIEjJglUjUlZD4kc'
        
        try:
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNzc4fQ:1eeU6f:GYjPfRTPYLfaZDjwaE8iwddQ4A4'
        
        try:
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNzc5fQ:1eeU6f:7LdL7ei2w_57jAmrMEsVh_1GVeg'
        
        try:
            pass
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
