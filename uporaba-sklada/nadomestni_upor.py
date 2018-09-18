# =============================================================================
# Nadomestni upor
#
# Kot je dobro znano iz elektrotehnike, nadomestni upor dveh zaporedno
# vezanih upornikov izračunamo po formuli $R = R_1 + R_2$, nadomestni
# upor dveh vzporedno vezanih upornikov pa je $1/R = 1/R_1 + 1/R_2$.
# =====================================================================@010420=
# 1. podnaloga
# Napišite funkcijo `nadomestni_upor(r1, r2, tipV)`, ki kot argumenta dobi
# dve števili `r1` in `r2` (tj. upor obeh upornikov) in tip vezave `tipV`,
# ki je bodisi znak `'V'` bodisi znak `'Z'`. Funkcija naj vrne nadomestni
# upor vezja.
# Pozor: nekateri uporniki so vezani kratkostično in imajo upor 0.
# (Upor dveh vzporedno vezanih upornikov, od katerih ima vsaj en upor 0, je 0.)
# 
#     >>> nadomestni_upor(3, 5, 'Z')
#     8
#     >>> nadomestni_upor(3, 0, 'V')
#     0
#     >>> nadomestni_upor(2, 5, 'V')
#     1.875
# =============================================================================
from sklad import Sklad

def nadomestni_upor(r1, r2, tipV):
    '''Izračuna nadomestni upor.'''
    if tipV == 'Z':
        return r1 + r2
    elif 0 not in (r1, r2): # Vzporedna vezava
        return (r1 * r2) / (r1 + r2)
    else:
        return 0
# =====================================================================@010421=
# 2. podnaloga
# Sestavite funkcijo `upor_vezja(niz)`, ki izračuna nadomestni upor vezja.
# Vezje je podano kot niz v "RPN notaciji": operandom (tj. vrednosti uporov)
# sledi operator (tj. način vezave, `'V'` ali `'Z'`).
# 
# Analizirajmo vezje `'3 5 Z 0 V 3 2 Z V'`: 
# Niz `'3 5 Z'` tako pomeni, da sta zaporedno vezana upornika z upornostma
# 3 in 5 (ki ju lahko nadomestimo z enim upornikom z upornostjo 8). Skratka,
# dobimo vezje `'8 0 V 3 2 Z V'`.
# V tem novem vezju niz `'8 0 V'` pomeni, da sta vzporedno vezana upornika z
# upornostma 8 in 0. Vzporedna vezava, ki vsebuje kratkostični upornik, je
# kratkostična, zato je 0 nadomestni upor vezja `'8 0 V'`. Skratka, dobimo
# vezje `'0 3 2 Z V'`.
# Niz `'3 2 Z'` pomeni, da sta zaporedno vezana upornika z upornostma 3 in 2
# (in torej z nadomestno upornostjo 5). Če upoštevamo še to, potem dobimo
# vezje `'0 5 V'`, kar na koncu da rezultat 0.
# 
#     >>> upor_vezja('3 5 Z 0 V 3 2 Z V')
#     0
# 
# Predpostavite lahko, da v nizu `niz` nastopajo (poleg znakov `'V'`, `'Z'`
# in `' '`) le nenegativna cela števila.
# =============================================================================
def upor_vezja(niz):
    '''Izračuna upor vezja s pomočjo sklada.'''
    print(niz)
    sklad = Sklad()
    for znak in niz.split():
        if znak in 'VZ':
            drugiEl = sklad.poberi()
            prviEl = sklad.poberi()
            sklad.vstavi(nadomestni_upor(float(prviEl), float(drugiEl), znak))
        else: # Imamo število
            sklad.vstavi(float(znak))
    return sklad.poberi()
# =====================================================================@010422=
# 3. podnaloga
# Napišite še funkcijo `sestavi_racun(niz)`, ki namesto da izračuna
# nadomestni upor vezja sestavi račun, ki ga je potrebno izračunati,
# da dobimo nadomestni upor vezja.
# 
#     >>> sestavi_racun('3 5 Z 0 V 3 2 Z V')
#     '(1/(1/(3 + 5) + 1/0)^-1 + 1/(3 + 2))^-1'
# 
# _Namig_: Ali lahko nalogo rešite tako, da malenkost predelate rešitev
# prejšnje naloge?
# =============================================================================

# =====================================================================@010423=
# 4. podnaloga
# Stari električarski mački si račun poenostavijo na sledeč način: če je
# upor $R_a$ več kot 10-krat večji kot upor $R_b$, potem za nadomestni
# upor zaporedne vezave upornikov $R_a$ in $R_b$ vzamejo kar $R_a$, kot
# nadomestni upor vzporedne vezave pa kar upor $R_b$. Seveda pa pravilno
# razumejo vezavo, če je kakšen upor enak 0.
# 
# Sestavite funkcijo `stari_macki(niz)`, ki bo nadomestni upor vezja
# izračunala po "metodi starih mačkov".
# 
#     >>> stari_macki('2 30 Z 20 V 3 2 Z V')
#     3.5294117647058822
# =============================================================================





































































































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
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, use_globals=False):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            def visible_input(prompt=''):
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
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
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
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
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
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDQyMCwidXNlciI6MTE1fQ:1g1pYh:NjHrtPaxiE8dugbLnsYKkNff6Ao'
        try:
            test_data = [
                ("nadomestni_upor(3, 5, 'Z')", 8),
                ("nadomestni_upor(0, 0, 'Z')", 0),
                ("nadomestni_upor(3, 0, 'V')", 0),
                ("nadomestni_upor(0, 0, 'V')", 0),
                ("nadomestni_upor(0, 3, 'V')", 0),
                ("nadomestni_upor(3, 5, 'V')", 1.875),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDQyMSwidXNlciI6MTE1fQ:1g1pYh:_vdRub-TWvT38mv3KmDpwWnXb-w'
        try:
            test_data = [
                ("upor_vezja('3 5 Z')", 8),
                ("upor_vezja('3 5 Z 0 V')", 0),
                ("upor_vezja('3 2 Z')", 5),
                ("upor_vezja('3 5 Z 0 V 3 2 Z V')", 0),
                ("upor_vezja('2 30 Z 20 V 3 2 Z V')", 3.555555555555555),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDQyMiwidXNlciI6MTE1fQ:1g1pYh:hSdmU3AU0sS59uXYVo21Z_ZM0do'
        try:
            test_data = [
                ("sestavi_racun('3 5 Z')", '(3 + 5)'),
                ("sestavi_racun('3 5 Z 0 V')", '(1/(3 + 5) + 1/0)^-1'),
                ("sestavi_racun('3 2 Z')", '(3 + 2)'),
                ("sestavi_racun('3 5 Z 0 V 3 2 Z V')", '(1/(1/(3 + 5) + 1/0)^-1 + 1/(3 + 2))^-1'),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDQyMywidXNlciI6MTE1fQ:1g1pYh:AHRtzbPCX_I_YIcXn15Qs5dpmrQ'
        try:
            test_data = [
                ("stari_macki('3 5 Z')", 8),
                ("stari_macki('3 5 Z 0 V')", 0),
                ("stari_macki('3 2 Z')", 5),
                ("stari_macki('3 5 Z 0 V 3 2 Z V')", 0),
                ("stari_macki('2 30 Z 20 V 3 2 Z V')", 3.5294117647058822),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
            print('Posodabljam datoteko... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Stara datoteka je bila preimenovana v {0}.'.format(backup_filename))
            print('Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
