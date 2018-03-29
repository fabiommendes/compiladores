import re
import io
import sys
import argparse
import configparser


class Section:
    def __init__(self, title, regex='', enabled=True, size=None, intro='',
                 help='', weight=1,
                 accept=(), reject=(), accept_extra=(), reject_extra=()):
        self.title = title
        self.regex = regex
        self.enabled = enabled
        self.size = len(regex) if size is None else int(size)
        self.intro = intro.strip()
        self.help = help.strip()
        self.accept = accept
        self.reject = reject
        self.accept_extra = accept_extra
        self.reject_extra = reject_extra
        self.weight = float(weight)

    def __str__(self):
        file = io.StringIO()
        self.print(file)
        return file.getvalue()

    def print(self, file=None):
        msg = (lambda *args: print(*args, file=file))
        if self.intro:
            msg('#')
            msg(comment(self.intro) + '\n#\n')
        msg('[%s]' % self.title)
        if self.help:
            msg(comment(self.help))
        msg('regex =', self.regex)
        msg('size =', self.size)
        if self.accept:
            msg('accept =', '; '.join(self.accept))
        if self.reject:
            msg('reject =', '; '.join(self.reject))
        if self.accept_extra:
            msg('accept_extra =', '; '.join(self.accept_extra))
        if self.reject_extra:
            msg('reject_extra =', '; '.join(self.reject_extra))
        if self.enabled is False:
            msg('enabled = no')
        if self.weight != 1:
            msg('weight =', self.weight)

    def get_errors(self):
        try:
            regex = re.compile(self.regex)
        except:
            return ['Invalid regex: %s' % self.regex]

        errors = []
        for st in self.accept:
            if not regex.fullmatch(st):
                errors.append(
                    'Missing match: %r (must match this string)' % st)
        for st in self.reject:
            if regex.fullmatch(st):
                errors.append(
                    'reject match: %r (should not match this string)' % st)
        return errors

    def as_ref_section(self):
        return Section(
            title=self.title,
            enabled=False,
            size=self.size,
            intro=self.intro,
            help=self.help,
            accept=self.accept,
            reject=self.reject,
            weight=self.weight,
        )


def comment(st):
    return '\n'.join('# ' + x for x in st.splitlines())


def read_file(path):
    conf = configparser.ConfigParser()
    conf.read(path)
    return [parse_section(conf[section], section)
            for section in conf.sections()]


def parse_section(sec, title):
    booleans = {'true': True, 'false': False, 'yes': True, 'no': False}
    data = dict(sec)
    data['accept'] = parse_examples(data.get('accept', ''))
    data['reject'] = parse_examples(data.get('reject', ''))
    if 'enabled' in data:
        data['enabled'] = booleans[data['enabled'].lower()]
    return Section(title=title, **data)


def parse_examples(st):
    return [s for s in st.strip().split('; ') if s]


def write_ref_file(from_path):
    sections = []
    has_errors = False
    intro = 'REGEX TEXT'

    for sec in read_file(from_path):
        if sec.title == 'config':
            intro = sec.intro
            continue

        sections.append(str(sec.as_ref_section()))
        errors = sec.get_errors()
        if errors:
            has_errors = True
            print_errors(errors, sec.title)

    if has_errors:
        raise SystemExit('file has errors')
    else:
        print('#')
        print(comment(intro.strip()))
        print('#\n\n')
        print('\n\n'.join(sections))


def print_errors(errors, title):
    print('\n[%s]' % title, file=sys.stdout)
    for error in errors:
        print(error, file=sys.stdout)


def grade_file(file):
    print('GRADING FILE...')
    num_disabled = 0
    num_ok = 0
    num_partial = 0
    num_bad = 0
    grade = 0
    grade_total = 0

    for sec in read_file(file):
        if sec.title == 'config':
            continue
        
        grade_total += sec.weight

        if (not sec.enabled) or (sec.regex == ''):
            num_disabled += 1
        else:
            errors = sec.get_errors()
            if errors:
                num_bad += 1
                print_errors(errors, sec.title)
            elif len(sec.regex) > sec.size:
                num_partial += 1
                msg = '- Regex is too big (%s characters), should have at most %s'
                print('\n[%s]' % sec.title)
                print(msg % (len(sec.regex), sec.size))
                grade += sec.weight / 2
            else:
                num_ok += 1 
                grade += sec.weight

    print('\n\nFinished!')
    print('  - 100%    :', num_ok)
    print('  -  50%    :', num_partial)
    print('  - Error   :', num_bad)
    print('  - Disabled:', num_disabled)
    print('Final grade: %.0f%%' % (100 * grade / grade_total))


def main():
    parser = argparse.ArgumentParser(description='Grade test')
    parser.add_argument('file', help='input file')
    parser.add_argument('--student', '-s', action='store_const', const=True,
                        help='print file to pass to students')

    args = parser.parse_args()
    if args.student:
        write_ref_file(args.file)
    else:
        grade_file(args.file)


if __name__ == '__main__':
    main()
