# =============================================================================
# Ocenjevanje časovne zahtevnosti
#
# Dostikrat lahko časovno zahtevnost algoritma ocenimo že iz njegove izvorne
# kode.
# =====================================================================@011618=
# 1. podnaloga
# Dane naj bodo sledeče funkcije:
# 
#     def vsota1(n):
#         vsota = 0
#         for i in range(n):
#             for j in range(n):
#                 vsota += i + j
#         return vsota
#  
#     def vsota2(n):
#         vsota = 0
#         for i in range(n):
#             for j in range(100):
#                 vsota += i + j
#         return vsota
#  
#     def vsota3(n):
#         vsota = 0
#         for i in range(n):
#             for j in range(n):
#                 vsota += sum(range(i))
#         return vsota
# 
# V spremenljivko `potence1` shranite nabor potenc njihovih časovnih zahtevnosti
# v odvisnosti od vhoda $n$. Na primer, če bi imele funkcije časovne zahtevnosti
# $O(n^3)$, $O(n)$ in $O(n^4)$, bi v spremenljivko `potence1` shranili
# nabor `(3, 1, 4)`.
# =============================================================================
potence1 = (2, 1, 3)

# Ima 2 zanki, odvisni od n
def vsota1(n): # O(1)
    vsota = 0  # O(1)
    for i in range(n): # O(1) ali O(n)
        for j in range(n): # O(1) ali O(n)
            vsota += i + j # O(1)
    return vsota # O(1)

# Eno zanko, pogojeno z n
def vsota2(n):
    vsota = 0
    for i in range(n):
        for j in range(100):
            vsota += i + j
    return vsota

# 2 zanki, odvisni od n-ja + vgrajena funkcija v odvisnosti od i-ja, ki je odvisen od n-ja
def vsota3(n):
    vsota = 0
    for i in range(n):
        for j in range(n):
            vsota += sum(range(i))
    return vsota
# =====================================================================@011617=
# 2. podnaloga
# Dane naj bodo sledeče funkcije na seznamih:
# 
#     def poisci_max1(sez):
#         return sez.index(max(sez))
# 
#     def poisci_max2(sez):
#         najvecji = None
#         for i in range(len(sez)):
#             if najvecji is None or sez[i] > najvecji:
#                 najvecji_i = i
#                 najvecji = sez[i]
#         return najvecji_i
# 
#     def poisci_max3(sez):
#         for i in range(len(sez)):
#             if sez[i] == max(sez):
#                 return i
# 
# V spremenljivko `potence2` shranite nabor potenc njihovih časovnih zahtevnosti
# v odvisnosti od dolžine vhodnega seznama.
# =============================================================================

# Enkrat gremo čez seznam za dobiti max in še enkrat za indeks, torej O(n)
def poisci_max1(sez):
    return sez.index(max(sez))

# Enkrat gremo s for zanko čez vse elemente, torej  O(n)
def poisci_max2(sez):
    najvecji = None
    for i in range(len(sez)):
        if najvecji is None or sez[i] > najvecji:
            najvecji_i = i
            najvecji = sez[i]
    return najvecji_i

# Enkrat gremo z zanko čez vse elemente in znotraj VSAKIČ iščemo max, torej O(n^2)
def poisci_max3(sez):
    for i in range(len(sez)):
        if sez[i] == max(sez):
            return i

potence2 = (1, 1, 2)
# =====================================================================@011728=
# 3. podnaloga
# Dane naj bodo sledeče funkcije, ki izračunajo sled kvadratne matrike
# velikosti $n \times n$:
# 
#     def sled1(mat):
#         sled = 0
#         for i in range(len(mat)):
#              for j in range(len(mat)):
#                  if i == j:
#                      sled += mat[i][j]
#         return sled
# 
#     def sled2(mat):
#         sled = 0
#         for i in range(len(mat)):
#              sled += mat[i][i]
#         return sled
# 
#     def sled3(mat):
#         sled = 0
#         for i, vrstica in enumerate(mat):
#              sled += vrstica[i]
#         return sled
# 
# V spremenljivko `potence3` shranite nabor potenc njihovih časovnih zahtevnosti
# v odvisnosti od števila $n$.
# =============================================================================

# Enkrat for zanka za indekse i, enkrat za indekse j, torej O(n^2)
def sled1(mat):
    sled = 0
    for i in range(len(mat)):
         for j in range(len(mat)):
             if i == j:
                 sled += mat[i][j]
    return sled

# Enkrat for zanka za indekse i in to je to, torej O(n)
def sled2(mat):
    sled = 0
    for i in range(len(mat)):
         sled += mat[i][i]
    return sled

# Enkrat for zanka, enumerate pa izvedemo le enkrat, torej O(n)
def sled3(mat):
    sled = 0
    for i, vrstica in enumerate(mat):
         sled += vrstica[i]
    return sled

potence3 = (2, 1, 1)
# =====================================================================@011729=
# 4. podnaloga
# Dane naj bodo sledeče funkcije, ki iščejo dani element v urejenem seznamu:
# 
#     def poisci1(sez, x):
#         return x in sez
# 
#     def poisci2(sez, x):
#         for y in sez:
#             if x == y:
#                 return True
#         return False
#     
#     def poisci3(sez, x):
#         od, do = 0, len(sez)
#         while od < do:
#             sredina = (od + do) // 2
#             sredinski = sez[sredina]
#             if x == sredinski:
#                 return True
#             elif x < sredinski:
#                 do = sredina
#             elif x > sredinski:
#                 od = sredina + 1
#         return False
#     
#     def poisci4(sez, x, od=0, do=None):
#         if do is None:
#             do = len(sez)
#         if od == do:
#             return False
#         else:
#             sredina = (od + do) // 2
#             sredinski = sez[sredina]
#             if x == sredinski:
#                 return True
#             elif x < sredinski:
#                 return poisci4(sez, x, od, sredina)
#             elif x > sredinski:
#                 return poisci4(sez, x, sredina + 1, do)
#     
#     def poisci5(sez, x):
#         if not sez:
#             return False
#         else:
#             sredina = len(sez) // 2
#             sredinski = sez[sredina]
#             if x == sredinski:
#                 return True
#             elif x < sredinski:
#                 return poisci5(sez[:sredina], x)
#             elif x > sredinski:
#                 return poisci5(sez[sredina + 1:], x)
# 
# V spremenljivko `zahtevnosti4` shranite nabor njihovih časovnih zahtevnosti,
# v odvisnosti od dolžine seznama. Časovne zahtevnosti opišite z enim od nizov
#     'O(1)', 'O(n)', 'O(n^2)', 'O(log n)', 'O(n log n)', 'O(n^3)'.
# =============================================================================
zahtevnosti4 = ('O(n)', 'O(n)', 'O(log n)', 'O(log n)', 'O(n)')

# Gre čez vse elemente, torej O(n)
def poisci1(sez, x):
    return x in sez

# Ravno tako gre čez vse elemente, torej O(n)
def poisci2(sez, x):
    for y in sez:
        if x == y:
            return True
    return False

# Ker je seznam urejen, ga zmeraj prepolovi, torej O(log n)
def poisci3(sez, x):
    od, do = 0, len(sez)
    while od < do:
        sredina = (od + do) // 2
        sredinski = sez[sredina]
        if x == sredinski:
            return True
        elif x < sredinski:
            do = sredina
        elif x > sredinski:
            od = sredina + 1
    return False

# Podobna funkcija kot prejšnja, le da uporablja rekurzijo namesto zanke O(log n)
def poisci4(sez, x, od=0, do=None):
    if do is None:
        do = len(sez)
    if od == do:
        return False
    else:
        sredina = (od + do) // 2
        sredinski = sez[sredina]
        if x == sredinski:
            return True
        elif x < sredinski:
            return poisci4(sez, x, od, sredina)
        elif x > sredinski:
            return poisci4(sez, x, sredina + 1, do)

# Tu je problem, saj delamo rezine seznama. Kopiramo 1/2 seznama, nato 1/4, 1/8...
# Zahtevnost ni O(n log n), temveč O(n)
def poisci5(sez, x):
    if not sez:
        return False
    else:
        sredina = len(sez) // 2
        sredinski = sez[sredina]
        if x == sredinski:
            return True
        elif x < sredinski:
            return poisci5(sez[:sredina], x)
        elif x > sredinski:
            return poisci5(sez[sredina + 1:], x)




































































































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
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNjE4fQ:1eeU6Z:sG_uqzO27DYSwwic75QT4hnbfco'
        
        try:
            if not isinstance(potence1, tuple):
                Check.error('Spremenljivka potence1 ni nabor.')
            elif len(potence1) != 3:
                Check.error('Spremenljivka potence1 mora vsebovati 3 elemente.')
            elif not all(isinstance(potenca, int) for potenca in potence1):
                Check.error('Spremenljivka potence1 mora vsebovati samo cela števila.')
            elif not all(potenca >= 0 for potenca in potence1):
                Check.error('Spremenljivka potence1 mora vsebovati samo nenegativna števila.')
            Check.secret(potence1)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNjE3fQ:1eeU6Z:2Z2bG735f79jc3prfwOtG7TptX8'
        
        try:
            if not isinstance(potence2, tuple):
                Check.error('Spremenljivka potence2 ni nabor.')
            elif len(potence2) != 3:
                Check.error('Spremenljivka potence2 mora vsebovati 3 elemente.')
            elif not all(isinstance(potenca, int) for potenca in potence2):
                Check.error('Spremenljivka potence2 mora vsebovati samo cela števila.')
            elif not all(potenca >= 0 for potenca in potence2):
                Check.error('Spremenljivka potence2 mora vsebovati samo nenegativna števila.')
            Check.secret(potence2)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNzI4fQ:1eeU6Z:--BEcks3-eLM-yc-6efLwCX12vI'
        
        try:
            if not isinstance(potence3, tuple):
                Check.error('Spremenljivka potence3 ni nabor.')
            elif len(potence3) != 3:
                Check.error('Spremenljivka potence3 mora vsebovati 3 elemente.')
            elif not all(isinstance(potenca, int) for potenca in potence3):
                Check.error('Spremenljivka potence3 mora vsebovati samo cela števila.')
            elif not all(potenca >= 0 for potenca in potence3):
                Check.error('Spremenljivka potence3 mora vsebovati samo nenegativna števila.')
            Check.secret(potence3)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMTUsInBhcnQiOjExNzI5fQ:1eeU6Z:Npi9n1sPd9MOxOSkOSLlVHiEhXU'
        
        try:
            if not isinstance(zahtevnosti4, tuple):
                Check.error('Spremenljivka zahtevnosti4 ni nabor.')
            elif len(zahtevnosti4) != 5:
                Check.error('Spremenljivka zahtevnosti4 mora vsebovati 5 elementov.')
            else:
                for zahtevnost in zahtevnosti4:
                    if zahtevnost not in ['O(1)', 'O(n)', 'O(n^2)', 'O(log n)', 'O(n log n)', 'O(n^3)']:
                        Check.error('Zahtevnost {!r} ni pravilne oblike.'.format(zahtevnost))
                if zahtevnosti4[4] == 'O(log n)':
                    Check.error('Razmislite, koliko je časovna zahtevnost ustvarjanja rezin.')
            Check.secret(zahtevnosti4)
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
