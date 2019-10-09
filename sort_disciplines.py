import urllib.request
import json
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def filter_disciplines(disciplines):
    for i in range(len(disciplines)):
        disciplines[i] = remove_accents(disciplines[i]).lower()


def extract_disciplines_from_api():
    with urllib.request.urlopen("http://mwapi.herokuapp.com/disciplines") as url:
        data = json.loads(url.read().decode())
        name_disciplines = []
        for discipline in data:
            name_disciplines.append(discipline['name'])

    return name_disciplines


def write_file(filename, disciplines):
    file2write = open(filename, 'w')

    for discipline in disciplines:
        file2write.write(discipline.upper() + "\n")

    file2write.close()


def radix_sort_msd(L, i):
    # base case (list must already be sorted)
    if len(L) <= 1:
        return L

    # divide (first by length, then by lexicographical order of the first character)
    done_bucket = []
    buckets = [[] for x in range(256)]  # one for each element ascii

    for s in L:
        if i >= len(str(s)):
            done_bucket.append(s)
        else:
            buckets[ ord(s[i]) ].append(s)

    # conquer (recursively sort buckets)
    buckets = [ radix_sort_msd(b, i + 1) for b in buckets ]

    # marry (chain all buckets together)
    return done_bucket + [ b for blist in buckets for b in blist ]

def main():
    name_disciplines = extract_disciplines_from_api()
    filter_disciplines(name_disciplines)
    write_file('unsorted.txt', name_disciplines)
    sorted_disciplines = radix_sort_msd(name_disciplines, 0)
    write_file('sorted.txt', sorted_disciplines)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interruption')
