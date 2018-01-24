# =============================================================================
# Množice z iskalnimi drevesi
#
# Podatkovno strukturo množica lahko učinkovito predstavimo z iskalnim drevesom.
# V tej nalogi bomo najprej definirali nekaj pomožnih funkcij na drevesih, nato
# pa definirali razred `Mnozica`, ki podpira osnovne operacije na množicah.
# =====================================================================@011421=
# 1. podnaloga
# Sestavite funkcijo `vstavi_v_iskalno_drevo(drevo, x)`, ki v iskalno drevo na
# pravo mesto vstavi element `x` ter vrne novo drevo. Če je `x` enak podatku
# v korenu drevesa, naj funkcija vrne prvotno drevo.
# =============================================================================
from drevo import Drevo

def vstavi_v_iskalno_drevo(drevo, x):
    '''V iskalno drevo vstavi element x na pravo mesto.'''
    if drevo.prazno:
        return Drevo(x)
    if x == drevo.podatek:
        return drevo
    elif x > drevo.podatek:
        return Drevo(drevo.podatek, levo=drevo.levo, desno=vstavi_v_iskalno_drevo(drevo.desno, x))
    else:
        return Drevo(drevo.podatek, levo=vstavi_v_iskalno_drevo(drevo.levo, x), desno=drevo.desno)
# =====================================================================@011422=
# 2. podnaloga
# Sestavite funkcijo `ali_vsebuje(drevo, x)`, ki vrne `True`, če dano iskalno
# drevo vsebuje podatek `x`, in `False`, če ga ne.
# =============================================================================
def ali_vsebuje(drevo, x):
    '''Vrne, ali drevo vsebuje podatek x.'''
    if drevo.prazno:
        return False
    if drevo.podatek == x:
        return True
    elif ali_vsebuje(drevo.levo, x) or ali_vsebuje(drevo.desno, x):
        return True
    else:
        return False
# =====================================================================@011423=
# 3. podnaloga
# Z razredom `Mnozica` bomo predstavili nespremenljive množice, torej take, ki
# ne podpirajo metod za dodajanje in odstranjevanje elementov, le metode, ki
# izračunajo nove množice iz obstoječih. Vsako množico bomo predstavili z
# objektom, ki ima dva atributa: iskalnim drevesom elementov `_elementi` ter
# velikostjo `_velikost`.
# 
# Sestavite razred `Mnozica` z metodo `__init__`, ki mu za neobvezen prvi
# argument lahko podamo iterator začetnih elementov množice.
# =============================================================================
def vmesni_pregled(d):
    '''Generator vmesnega pregleda drevesa.'''
    if not d.prazno:
        yield from vmesni_pregled(d.levo)
        yield d.podatek
        yield from vmesni_pregled(d.desno)

class Mnozica:

    def __init__(self, *args):
        # Prazno drevo
        self._elementi = Drevo()
        self._velikost = 0

        iterator = []
        if len(args) == 1:
            iterator = args[0]

        # Dodajamo v drevo iz iteratorja
        for x in iterator:
            if not ali_vsebuje(self._elementi, x):
                self._elementi = vstavi_v_iskalno_drevo(self._elementi, x)
                self._velikost += 1

# =====================================================================@011424=
# 4. podnaloga
# Dodajte metodo `__iter__`, ki vrne iterator, ki našteva elemente množice od
# najmanjšega do največjega.
# =============================================================================
    def __iter__(self):
        '''Našteva elemente množice od najmanjšega do največjega.'''
        return vmesni_pregled(self._elementi)
# =====================================================================@011425=
# 5. podnaloga
# Za lepši prikaz dodajte še metodo `__str__`, ki vrne niz oblike
# `{el1, el2, ...}`, kjer so elementi množice našteti od najmanjšega do
# največjega.
# =============================================================================
    def __str__(self):
        '''Grafična predstavitev množice.'''
        niz = ''
        for x in iter(self):
            niz += repr(x) + ', ' # Mora biti repr
        niz = '{' + niz[:-2] + '}'
        return niz
# =====================================================================@011426=
# 6. podnaloga
# Za dostop do velikosti množice `mn` in iskanja elementov v njej bi sicer lahko
# napisali metodi `mn.velikost()` in `mn.vsebuje(x)`, vendar je bolj Pythonovsko,
# da definiramo metodi `__len__` in `__contains__`, da lahko pišemo kar `len(mn)`
# in `x in mn` oz. `x not in mn`. Definirajte ju.
# =============================================================================

# =====================================================================@011427=
# 7. podnaloga
# Definirajte še metodi `__or__` in `__and__`, ki sprejmeta dve množici ter
# vrneta njuno unijo in presek. Stvari naredite učinkovite tako, da upoštevate
# velikost množic.
# =============================================================================

# =====================================================================@011428=
# 8. podnaloga
# Kaj bi se zgodilo, če bi sestavili množico z `Mnozica(range(1000000))`? Ali
# bi bila taka podatkovna struktura učinkovita? Na vajah se bomo pogovorili o
# tem, kako lahko izboljšamo učinkovitost s tem, da uporabimo uravnotežena
# dvojiška drevesa.
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
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDIxfQ:1eeU6S:B8nn3I6vQXCa18toYtWnlWNy-K4'
        
        try:
            Check.equal('vstavi_v_iskalno_drevo(Drevo(), 5)', Drevo(5))
            Check.equal('vstavi_v_iskalno_drevo(Drevo(5), 4)', Drevo(5, levo=Drevo(4)))
            Check.equal('vstavi_v_iskalno_drevo(Drevo(5), 5)', Drevo(5))
            Check.equal('vstavi_v_iskalno_drevo(Drevo(5, levo=Drevo(4)), 7)', Drevo(5, levo=Drevo(4), desno=Drevo(7)))
            Check.equal('vstavi_v_iskalno_drevo(Drevo(5, levo=Drevo(4), desno=Drevo(7)), 6)', Drevo(5, levo=Drevo(4), desno=Drevo(7, levo=Drevo(6))))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDIyfQ:1eeU6S:vZKGOy8avfZ7wndbYOSQkFotBrs'
        
        try:
            Check.equal('ali_vsebuje(Drevo(), 5)', False)
            Check.equal('ali_vsebuje(Drevo(5, levo=Drevo(4), desno=Drevo(7)), 4)', True)
            Check.equal('ali_vsebuje(Drevo(5, levo=Drevo(4), desno=Drevo(7)), 5)', True)
            Check.equal('ali_vsebuje(Drevo(5, levo=Drevo(4), desno=Drevo(7)), 6)', False)
            Check.equal('ali_vsebuje(Drevo(5, levo=Drevo(4), desno=Drevo(7)), 7)', True)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDIzfQ:1eeU6S:Vl-_dZHyoTaQ__VcZZMVxnORrpo'
        
        try:
            Check.run([
                'mn = Mnozica()',
                'elementi = mn._elementi',
                'velikost = mn._velikost',
            ], {'elementi': Drevo(), 'velikost': 0})
            Check.run([
                'vsebuje_vse = all(ali_vsebuje(Mnozica([3, 4, 5])._elementi, x) for x in [3, 4, 5])',
                'velikost = Mnozica([3, 4, 5])._velikost',
            ], {'vsebuje_vse': True, 'velikost': 3})
            Check.run([
                "vsebuje_vse = all(ali_vsebuje(Mnozica('xy')._elementi, x) for x in 'xy')",
                "velikost = Mnozica('xy')._velikost",
            ], {'vsebuje_vse': True, 'velikost': 2})
            Check.run([
                "vsebuje_vse = all(ali_vsebuje(Mnozica('mama')._elementi, x) for x in 'mama')",
                "velikost = Mnozica('mama')._velikost",
            ], {'vsebuje_vse': True, 'velikost': 2})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDI0fQ:1eeU6S:ij9HvazI833e1eFT_coQLF_SyNA'
        
        try:
            Check.generator('iter(Mnozica())', [], should_stop=True)
            Check.generator('iter(Mnozica([10, 5, 0]))', [0, 5, 10], should_stop=True)
            Check.generator("iter(Mnozica('mama'))", ['a', 'm'], should_stop=True)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDI1fQ:1eeU6S:SpzcP0HI6GvTCplDDWQBmFpA9T0'
        
        try:
            Check.equal('str(Mnozica())', '{}')
            Check.equal('str(Mnozica([10, 5, 0]))', '{0, 5, 10}')
            Check.equal("str(Mnozica('mama'))", "{'a', 'm'}")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDI2fQ:1eeU6S:9rXwQ4hmOn2CBc8ZIu5aIEzzKBU'
        
        try:
            Check.equal('len(Mnozica())', 0)
            Check.equal('len(Mnozica([10, 5, 0]))', 3)
            Check.equal("len(Mnozica('mama'))", 2)
            Check.equal('3 in Mnozica()', False)
            Check.equal('5 in Mnozica([10, 5, 0])', True)
            Check.equal("'x' not in Mnozica('mama')", True)
            Check.equal("'m' in Mnozica('mama')", True)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDI3fQ:1eeU6S:i-rUkOu9Hd2jeMbKtdNisp39pDM'
        
        try:
            Check.equal('str(Mnozica([1, 2, 3]) | Mnozica([3, 4, 5]))', '{1, 2, 3, 4, 5}')
            Check.equal('str(Mnozica([1, 2, 3]) & Mnozica([3, 4, 5]))', '{3}')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNDI4fQ:1eeU6S:yN5FoNaFdNOwQ4GWda2HRzSxSfw'
        
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
