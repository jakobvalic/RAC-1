# =============================================================================
# Dijkstrov algoritem odstavnega tira
#
# Na predavanjih ste spoznali algoritem za izračun vrednosti aritmetičnega
# izraza, ki uporablja dva sklada: enega za vrednosti, drugega za operacije.
# Z nekaj prilagoditvami lahko ta algoritem pretvorimo v Dijkstrov
# [algoritem odstavnega tira](https://en.wikipedia.org/wiki/Shunting-yard_algorithm),
# ki upošteva tudi prednost operacij, zato nam v aritmetičnem izrazu ni treba
# pisati vseh oklepajev.
# 
# V spodnjih nalogah bomo aritmetične izraze predstavili z nizi, v katerih
# bodo členi ločeni z vsaj enim presledkom, operacije pa bomo omejili na
# `+`, `*` in `**`.
# =====================================================================@010888=
# 1. podnaloga
# Najprej potrebujemo dve pomožni funkciji:
# 
# - `cleni_izraza(izraz)`, ki niz `izraz` po presledkih razbije na člene, ter
# - `izracunaj(a, op, b)`, ki operacijo `op` uporabi na številih `a` in `b`.
# 
#     >>> cleni_izraza(' ( 2 + 4 ) + 6 ')
#     ['(', '2', '+', '4', ')', '+', '6']
#     >>> izracunaj(2, '+', 4)
#     6
#     >>> izracunaj(2, '**', 4)
#     16
# =============================================================================
import ast
from Sklad import Sklad

def cleni_izraza(izraz):
    return izraz.split(' ')[1:-1]

def izracunaj(st1, op, st2):
    """Izračuna rezultat operacije."""
    if op == '+':
        return st1 + st2
    elif op == '*':
        return st1 * st2
    else:
        return st1 ** st2
# =====================================================================@010889=
# 2. podnaloga
# Pogost korak pri algoritmu je, da s sklada operacij poberemo operacijo
# (predstavljeno z nizom), s sklada vrednosti dve vrednosti (predstavljeni s
# števili), nato pa na sklad vrednosti vrnemo vrednost izračuna (prestavljeno
# s številom). Sestavite funkcijo `izvedi_racun(sklad_operacij, sklad_vrednosti)`,
# ki izvede zgornji korak.
# 
#     >>> sklad_operacij = Sklad()
#     >>> sklad_vrednosti = Sklad()
#     >>> sklad_vrednosti.vstavi(1)
#     >>> sklad_vrednosti.vstavi(2)
#     >>> sklad_vrednosti.vstavi(3)
#     >>> sklad_operacij.vstavi('+')
#     >>> sklad_operacij.vstavi('*')
#     >>> print(sklad_operacij)
#     DNO : + : * : VRH
#     >>> print(sklad_vrednosti)
#     DNO : 1 : 2 : 3 : VRH
#     >>> izvedi_racun(sklad_operacij, sklad_vrednosti)
#     >>> print(sklad_operacij)
#     DNO : + : VRH
#     >>> print(sklad_vrednosti)
#     DNO : 1 : 6 : VRH
#     >>> izvedi_racun(sklad_operacij, sklad_vrednosti)
#     >>> print(sklad_operacij)
#     DNO : VRH
#     >>> print(sklad_vrednosti)
#     DNO : 7 : VRH
# =============================================================================
def izvedi_racun(sklad_operacij, sklad_vrednosti):
    '''Pobere dve vrednosti s sklada vrednosti in eno operacijo s sklada operacij.
    Rezultat shrani nazaj na sklad vrednosti.'''
    op = sklad_operacij.poberi()
    st2 = sklad_vrednosti.poberi()
    st1 = sklad_vrednosti.poberi()
    sklad_vrednosti.vstavi(izracunaj(st1, op, st2))
    return  sklad_vrednosti
# =====================================================================@010886=
# 3. podnaloga
# Za začetek si oglejmo enostaven primer, ko so vsi podizrazi v oklepajih in
# dvoma glede vrstnega reda operacij ni. Sestavite funkcijo
# `vrednost_z_vsemi_oklepaji(izraz)`, ki izračuna in vrne vrednost izraza,
# predstavljenega z nizom `izraz`, zapisanega v običajni obliki z vsemi
# oklepaji. Pri tem sledite algoritmu s predavanj.
# 
#     >>> vrednost_z_vsemi_oklepaji('( 2 + 4 )')
#     6
#     >>> vrednost_z_vsemi_oklepaji('( ( 10 + 5 ) * ( 3 + 7 ) )')
#     150
# =============================================================================
def vrednost_z_vsemi_oklepaji(izraz):
    # pregledujemo izraz:
    # ko naletimo na vrednost:
    # jo damo na sklad vrednosti
    # ko naletimo na operator:
    # ga damo na sklad operatorjev
    # ko naletimo na oklepaj:
    # ga preskočimo
    # ko naletimo na zaklepaj:
    # izvedemo račun
    sklad_vrednosti = Sklad()
    sklad_operacij = Sklad()
    for clen in cleni_izraza(izraz):
        if clen == '(':
            continue
        elif clen == ')':
            sklad_vrednosti = izvedi_racun(sklad_operacij, sklad_vrednosti)
        elif clen in ['*', '+', '**']:
            sklad_operacij.vstavi(clen)
        else:
            sklad_vrednosti.vstavi(int(clen))
    return sklad_vrednosti.poberi()
# =====================================================================@010890=
# 4. podnaloga
# Glavna razlika med zgornjim in Dijkstrovim algoritmom je, da račune izvedemo
# tudi takrat, ko naletimo na operator, ki nima prednosti.
# 
# Sestavite funkcijo `sklad_ima_prednost(sklad_operacij, op)`, ki vrne `True`,
# kadar je na skladu operacij levo asociativna operacija, ki ima prioriteto
# višjo ali enako operatorju `op`.
# 
#     >>> sklad_operacij = Sklad()
#     >>> print(sklad_ima_prednost(sklad_operacij, '+'))
#     >>> False
#     >>> sklad_operacij.vstavi('*')
#     >>> print(sklad_ima_prednost(sklad_operacij, '*'))
#     >>> True
#     >>> print(sklad_ima_prednost(sklad_operacij, '**'))
#     >>> False
#     >>> sklad_operacij.vstavi('**')
#     >>> print(sklad_ima_prednost(sklad_operacij, '+'))
#     >>> False
# =============================================================================

# =====================================================================@010887=
# 5. podnaloga
# Sestavite funkcijo `vrednost(izraz)`, ki izračuna in vrne vrednost izraza,
# predstavljenega z nizom `izraz`. Pri tem lahko sledite algoritmu, opisanemu na
# <https://en.wikipedia.org/wiki/Shunting-yard_algorithm#The_algorithm_in_detail>.
# 
#     >>> vrednost('( 2 + 4 ) * 3')
#     18
#     >>> vrednost('2 + 4 * 3')
#     14
#     >>> vrednost('2 * 4 + 3')
#     11
# =============================================================================
def vrednost(izraz):
    # pregledujemo izraz:
        # ko naletimo na vrednost:
            # jo damo na sklad vrednosti
        # ko naletimo na operator:
            # dokler je na vrhu sklada operacija s prednostjo:
                # izvedi račun na skladu 
            # damo operator na sklad operatorjev
        # ko naletimo na oklepaj:
            # ga damo na sklad operatorjev
        # ko naletimo na zaklepaj:
            # dokler na vrhu sklada ni oklepaja:
                # izvedemo račun na skladu
            # odstranimo zaklepaj
    # dokler sklad operacij ni prazen:
        # izvedemo račun na skladu
        pass




































































































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
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDg4OCwidXNlciI6MTE1fQ:1g1pYh:-3xneUo6_qLKMWcfmTeTfkA92Sk'
        try:
            Check.equal("cleni_izraza(' ( 2 + 4 ) + 6 ')", ['(', '2', '+', '4', ')', '+', '6'])
            Check.equal("izracunaj(2, '+', 4)", 6)
            Check.equal("izracunaj(2, '**', 4)", 16)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDg4OSwidXNlciI6MTE1fQ:1g1pYh:tRdlNlFDzf-bVTzYnQTBaBH238s'
        try:
            Check.run([
                "sklad_operacij = Sklad()",
                "sklad_vrednosti = Sklad()",
                "sklad_vrednosti.vstavi(1)",
                "sklad_vrednosti.vstavi(2)",
                "sklad_vrednosti.vstavi(3)",
                "sklad_operacij.vstavi('+')",
                "sklad_operacij.vstavi('*')",
                "so1 = str(sklad_operacij)",
                "sv1 = str(sklad_vrednosti)",
                "izvedi_racun(sklad_operacij, sklad_vrednosti)",
                "so2 = str(sklad_operacij)",
                "sv2 = str(sklad_vrednosti)",
                "izvedi_racun(sklad_operacij, sklad_vrednosti)",
                "so3 = str(sklad_operacij)",
                "sv3 = str(sklad_vrednosti)",
            ], {
                'so1': "DNO : + : * : VRH",
                'sv1': "DNO : 1 : 2 : 3 : VRH",
                'so2': "DNO : + : VRH",
                'sv2': "DNO : 1 : 6 : VRH",
                'so3': "DNO : VRH",
                'sv3': "DNO : 7 : VRH",
            })
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDg4NiwidXNlciI6MTE1fQ:1g1pYh:a9xOuTDRADaA4huSKGh8hJiwU8U'
        try:
            Check.equal("vrednost_z_vsemi_oklepaji('( 2 + 4 )')", 6)
            Check.equal("vrednost_z_vsemi_oklepaji('( 2 ** ( 2 + 4 ) )')", 64)
            Check.equal("vrednost_z_vsemi_oklepaji('( ( 2 + 4 ) ** 2 )')", 36)
            Check.equal("vrednost_z_vsemi_oklepaji('( ( 10 + 5 ) + ( 3 * 7 ) )')", 36)
            Check.equal("vrednost_z_vsemi_oklepaji('( ( 10 + 5 ) * ( 3 + 7 ) )')", 150)
            Check.equal("vrednost_z_vsemi_oklepaji('( 1 * ( 3 + ( 5 * ( 7 + 9 ) ) ) )')", 83)
            Check.equal("vrednost_z_vsemi_oklepaji('( ( 1 * ( 3 + ( 5 * ( 7 + 9 ) ) ) ) + ( 2 * ( 4 + ( 6 * ( 8 + 10 ) ) ) ) )')", 307)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDg5MCwidXNlciI6MTE1fQ:1g1pYh:fZZK6Gi4mPZmEhKRTkjT7ahfJGI'
        try:
            Check.run([
                "sklad_operacij = Sklad()",
                "p1 = sklad_ima_prednost(sklad_operacij, '+')",
                "sklad_operacij.vstavi('*')",
                "p2 = sklad_ima_prednost(sklad_operacij, '*')",
                "p3 = sklad_ima_prednost(sklad_operacij, '**')",
                "sklad_operacij.vstavi('**')",
                "p4 = sklad_ima_prednost(sklad_operacij, '+')",
            ], {
                'p1': False,
                'p2': True,
                'p3': False,
                'p4': False,
            })
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxMDg4NywidXNlciI6MTE1fQ:1g1pYh:eI-JJrmW_Yf_hDdNmzYuSRghPBc'
        try:
            Check.equal("vrednost('( 2 + 4 ) * 3')", 18)
            Check.equal("vrednost('2 + 4 * 3')", 14)
            Check.equal("vrednost('2 * 4 + 3')", 11)
            Check.equal("vrednost('2 ** 4 ** 3')", 18446744073709551616)
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
