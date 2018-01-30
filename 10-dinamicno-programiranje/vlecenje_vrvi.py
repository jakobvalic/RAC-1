# =============================================================================
# Vlečenje vrvi
#
# Udeleženci piknika bodo vlekli vrv. So različnih spolov, starosti in
# mas, zato sprva niso vedeli, kako bi se pravično razdelili v dve
# skupini. Sklenili so, da je najpravičnejša razdelitev takšna, da bosta
# imeli obe skupini enako skupno težo, na število članov skupin pa se
# sploh ne bodo ozirali. Včasih dveh skupin s popolnoma enakima masama
# ni mogoče sestaviti, zato iščejo takšno razdelitev, da bo razlika med
# masama skupin čim manjša. Vsak udeleženec nam je zaupal svojo  maso v
# kilogramih in sicer jo je zaokrožil na najbližje celo število.
# =====================================================================@010512=
# 1. podnaloga
# Sestavite funkcijo `razdeli(mase)`, ki dobi seznam mas udeležencev in
# vrne skupno maso manjše od skupin pri najbolj pravični delitvi. Ta funkcija
# naj bo rekurzivna in naj pregleda vse možnosti. (Kaj so vse možnosti in
# koliko jih je?) Zgled:
# 
#     >>> razdeli([95, 82, 87, 102, 75])
#     197
# 
# _Komentar_: Najbolj pravično razdelitev dosežemo, če damo udeleženca
# z masama 102 in 95 skupaj, vsi ostali pa tvorijo drugo skupino.
# =============================================================================
def moznosti(mase):
    '''Rekurzivno pregleda vse možnosti za razporejanje v dve skupini.'''
    razporeditveSprvim = []
    if len(mase) == 0:
        return [(0, 0)]
    razporeditve = moznosti(mase[1:])
    for (skupina1, skupina2) in razporeditve:
        razporeditveSprvim.append((skupina1 + mase[0], skupina2)) # Prvega damo v prvo skupino
        razporeditveSprvim.append((skupina1, skupina2 + mase[0])) # Prvega damo v drugo skupino
    return razporeditveSprvim

def razdeli(mase):
    '''Vrne maso manjše od skupin.'''
    razporeditve = moznosti(mase)
    urejeneRazlike = sorted(razporeditve, key=lambda par:abs(par[1] - par[0]))
    return min(urejeneRazlike[0])

# =====================================================================@010513=
# 2. podnaloga
# Če zgornjo rešitev preizkusite na seznamih dolžine 25 ali več, boste
# ugotovili, da deluje izjemno počasi. Kakšna je njena časovna zahtevnost?
# 
# Nalogo bomo rešili še z dinamičnim programiranjem. Gre za tako imenovani
# _problem 0-1 nahrbtnika_. Izkoristili bomo dejstvo, da mase ljudi ne
# morejo biti poljubno velike (največja dokumentirana masa človeka je 635 kg)
# in da so celoštevilske. Pri sestavljanju skupin lahko dosežemo enako
# maso na različne načine.
# 
# Sestavite funkcijo `razdeli_dinamicno(mase)`, ki naredi isto kot prejšnja
# funkcija, le da se reševanja tokrat lotite z dinamičnim programiranjem.
# Zgled:
# 
#     >>> razdeli_dinamicno([95, 82, 87, 102, 75])
#     197
# 
# Funkcijo preizkusite na seznamu dolžine 50 in na seznamu dolžine 100.
# =============================================================================
def razdeli_dinamicno(mase):
    '''Razdeli mase z dinamičnim programiranjem, 0-1 nahrbtnikom.'''

# =====================================================================@010514=
# 3. podnaloga
# Prejšnja funkcija nam izračuna velikost skupine, nič pa ne izvemo o tem,
# kdo so udeleženci, ki tvorijo to skupino. Sestavite še funkcijo
# `razdeli_udelezence(mase)`, ki vrne seznam mas udeležencev, ki bodo
# tvorili manjšo od obeh skupin. Če je rešitev več, lahko funkcija vrne
# katerekoli rešitev. Zgled:
# 
#     >>> razdeli_udelezence([95, 82, 87, 102, 75])
#     [102, 95]
# 
# _Namig:_ Predelajte prejšnjo funkcijo, tako da bo iz nahrbtnika razvidno,
# kateri udeleženci morajo biti v skupini.
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
        
        try:
            test_data = [
                ("""razdeli([95, 82, 87, 102, 75])""", 197),
                ("""razdeli([60, 120])""", 60),
                ("""razdeli([80])""", 0),
                ("""razdeli([])""", 0),
                ("""razdeli([73, 91, 73, 80, 105, 71, 82, 102, 91, 76])""", 422),
                ("""razdeli([89, 86, 76, 101, 74, 109, 119, 102, 87, 111, 107, 115])""", 588),
                ("""razdeli([103, 80, 91, 120, 100, 106, 117, 119, 70, 82, 107, 85, 85])""", 632),
                ("""razdeli([114, 91, 72, 84, 97, 114, 97, 119, 106, 81, 86, 98, 72, 83])""", 657),
                ("""razdeli([115, 120, 89, 105, 102, 100, 101, 98, 106, 104, 86, 90, 100, 70, 74])""", 730),
                ("""razdeli([119, 72, 80, 111, 87, 84, 111, 76, 104, 73, 90, 78, 112, 82, 105, 76, 100, 98])""", 829),
                ("""razdeli([92, 89, 83, 91, 87, 110, 119, 119, 89, 96, 113, 82, 79, 97, 114, 84, 70, 90, 97])""", 900),
                ("""razdeli([98, 99, 103, 72, 117, 88, 93, 70, 78, 90, 104, 96, 101, 79, 119, 105, 107, 109, 71, 93])""", 946),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break  # Test has failed.
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ("""razdeli_dinamicno([95, 82, 87, 102, 75])""", 197),
                ("""razdeli_dinamicno([60, 120])""", 60),
                ("""razdeli_dinamicno([80])""", 0),
                ("""razdeli_dinamicno([])""", 0),
                ("""razdeli_dinamicno([73, 91, 73, 80, 105, 71, 82, 102, 91, 76])""", 422),
                ("""razdeli_dinamicno([89, 86, 76, 101, 74, 109, 119, 102, 87, 111, 107, 115])""", 588),
                ("""razdeli_dinamicno([103, 80, 91, 120, 100, 106, 117, 119, 70, 82, 107, 85, 85])""", 632),
                ("""razdeli_dinamicno([114, 91, 72, 84, 97, 114, 97, 119, 106, 81, 86, 98, 72, 83])""", 657),
                ("""razdeli_dinamicno([115, 120, 89, 105, 102, 100, 101, 98, 106, 104, 86, 90, 100, 70, 74])""", 730),
                ("""razdeli_dinamicno([119, 72, 80, 111, 87, 84, 111, 76, 104, 73, 90, 78, 112, 82, 105, 76, 100, 98])""", 829),
                ("""razdeli_dinamicno([92, 89, 83, 91, 87, 110, 119, 119, 89, 96, 113, 82, 79, 97, 114, 84, 70, 90, 97])""", 900),
                ("""razdeli_dinamicno([98, 99, 103, 72, 117, 88, 93, 70, 78, 90, 104, 96, 101, 79, 119, 105, 107, 109, 71, 93])""", 946),
                ("""razdeli_dinamicno([70, 78, 88, 80, 101, 109, 102, 97, 70, 114, 79, 77, 103, 81, 95, 118, 85, 82, 106, 94, 117, 114, 87, 104, 101, 112, 84, 95, 73, 120, 71, 120, 89, 74, 80, 76, 115, 118, 110, 115, 74, 117, 95, 103, 119, 99, 105, 100, 88, 101])""", 2402),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break  # Test has failed.
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ("""razdeli_udelezence([95, 82, 87, 102, 75])""", [102, 95]),
                ("""razdeli_udelezence([60, 120])""", [60]),
                ("""razdeli_udelezence([80])""", []),
                ("""razdeli_udelezence([])""", []),
                ("""razdeli_udelezence([73, 91, 73, 80, 105, 71, 82, 102, 91, 76])""", [105, 80, 73, 91, 73]),
                ("""razdeli_udelezence([89, 86, 76, 101, 74, 109, 119, 102, 87, 111, 107, 115])""", [111, 119, 109, 74, 86, 89]),
                ("""razdeli_udelezence([103, 80, 91, 120, 100, 106, 117, 119, 70, 82, 107, 85, 85])""", [70, 119, 117, 106, 100, 120]),
                ("""razdeli_udelezence([114, 91, 72, 84, 97, 114, 97, 119, 106, 81, 86, 98, 72, 83])""", [86, 81, 106, 114, 84, 72, 114]),
                ("""razdeli_udelezence([115, 120, 89, 105, 102, 100, 101, 98, 106, 104, 86, 90, 100, 70, 74])""", [98, 101, 102, 105, 89, 120, 115]),
                ("""razdeli_udelezence([119, 72, 80, 111, 87, 84, 111, 76, 104, 73, 90, 78, 112, 82, 105, 76, 100, 98])""", [78, 90, 104, 76, 84, 87, 111, 80, 119]),
                ("""razdeli_udelezence([92, 89, 83, 91, 87, 110, 119, 119, 89, 96, 113, 82, 79, 97, 114, 84, 70, 90, 97])""", [113, 89, 119, 119, 110, 87, 91, 83, 89]),
                ("""razdeli_udelezence([98, 99, 103, 72, 117, 88, 93, 70, 78, 90, 104, 96, 101, 79, 119, 105, 107, 109, 71, 93])""", [96, 104, 78, 70, 93, 88, 117, 103, 99, 98]),
                ("""razdeli_udelezence([70, 78, 88, 80, 101, 109, 102, 97, 70, 114, 79, 77, 103, 81, 95, 118, 85, 82, 106, 94, 117, 114, 87, 104, 101, 112, 84, 95, 73, 120, 71, 120, 89, 74, 80, 76, 115, 118, 110, 115, 74, 117, 95, 103, 119, 99, 105, 100, 88, 101])""", [95, 112, 101, 104, 114, 117, 94, 106, 82, 85, 118, 95, 81, 103, 77, 79, 114, 97, 102, 109, 101, 80, 88, 78, 70]),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break  # Test has failed.
            
            
            #test_data = [
            #    ([95, 82, 87, 102, 75], 197),
            #    ([60, 120], 60),
            #    ([80], 0),
            #    ([], 0),
            #    ([73, 91, 73, 80, 105, 71, 82, 102, 91, 76], 422),
            #    ([89, 86, 76, 101, 74, 109, 119, 102, 87, 111, 107, 115], 588),
            #    ([103, 80, 91, 120, 100, 106, 117, 119, 70, 82, 107, 85, 85], 632),
            #    ([114, 91, 72, 84, 97, 114, 97, 119, 106, 81, 86, 98, 72, 83], 657),
            #    ([115, 120, 89, 105, 102, 100, 101, 98, 106, 104, 86, 90, 100, 70, 74], 730),
            #    ([119, 72, 80, 111, 87, 84, 111, 76, 104, 73, 90, 78, 112, 82, 105, 76, 100, 98], 829),
            #    ([92, 89, 83, 91, 87, 110, 119, 119, 89, 96, 113, 82, 79, 97, 114, 84, 70, 90, 97], 900),
            #    ([98, 99, 103, 72, 117, 88, 93, 70, 78, 90, 104, 96, 101, 79, 119, 105, 107, 109, 71, 93], 946),
            #    ([70, 78, 88, 80, 101, 109, 102, 97, 70, 114, 79, 77, 103, 81, 95, 118, 85, 82, 106, 94, 117, 114, 87, 104, 101, 112, 84, 95, 73, 120, 71, 120, 89, 74, 80, 76, 115, 118, 110, 115, 74, 117, 95, 103, 119, 99, 105, 100, 88, 101], 2402),
            #]
            #vse_ok = True
            #for udelezenci, skup_masa in test_data:
            #    results = Check.execute("""sol = razdeli_udelezence({0!r})""".format(udelezenci))
            #    user = results['env']['sol']
            #    if sum(user) != skup_masa:
            #        Check.error('Skupna masa udeležencev, ki jih vrne razdeli_udelezence({0!r}), je neustrezna.', udelezenci)
            #        vse_ok = False
            #    else:
            #        d = dict()
            #        for m in udelezenci:
            #            if m not in d:
            #                d[m] = 0
            #            d[m] += 1
            #        for x in user:
            #            if x not in d:
            #                Check.error('Klic razdeli_udelezence({0!r}) vrne {1}, toda mase {2} nima nobeden.', udelezenci, user, x)
            #                vse_ok = False
            #                break
            #            d[x] -= 1
            #            if d[x] < 0:
            #                Check.error('Klic razdeli_udelezence({0!r}) vrne {1}, kjer se masa {2} pojavi prevečkrat.', udelezenci, user, x)
            #                vse_ok = False
            #                break
            #    if not vse_ok:
            #        break
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
