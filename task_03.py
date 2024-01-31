import timeit
from boyer_moore import boyer_moore
from knuth_morris_pratt import knuth_morris_pratt
from rabin_karp import rabin_karp


def read_text_from_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


text1 = read_text_from_file("text_01.txt")
text2 = read_text_from_file("text_02.txt")

substring1 = "доступ"
substring2 = "some made up substring"

t1_bm = timeit.timeit(lambda: boyer_moore(text1, substring1), number=1000)
t1_kmp = timeit.timeit(lambda: knuth_morris_pratt(text1, substring1), number=1000)
t1_rk = timeit.timeit(lambda: rabin_karp(text1, substring1), number=1000)

t2_bm = timeit.timeit(lambda: boyer_moore(text2, substring1), number=1000)
t2_kmp = timeit.timeit(lambda: knuth_morris_pratt(text2, substring1), number=1000)
t2_rk = timeit.timeit(lambda: rabin_karp(text2, substring1), number=1000)

t1_bm_fake = timeit.timeit(lambda: boyer_moore(text1, substring2), number=1000)
t1_kmp_fake = timeit.timeit(lambda: knuth_morris_pratt(text1, substring2), number=1000)
t1_rk_fake = timeit.timeit(lambda: rabin_karp(text1, substring2), number=1000)

t2_bm_fake = timeit.timeit(lambda: boyer_moore(text2, substring2), number=1000)
t2_kmp_fake = timeit.timeit(lambda: knuth_morris_pratt(text2, substring2), number=1000)
t2_rk_fake = timeit.timeit(lambda: rabin_karp(text2, substring2), number=1000)

print("Results for text1:")
print(f"Real substring: BM={t1_bm:.5f}, KMP={t1_kmp:.5f}, RK={t1_rk:.5f}")
print(
    f"Fake substring: BM={t1_bm_fake:.5f}, KMP={t1_kmp_fake:.5f}, RK={t1_rk_fake:.5f}"
)

print("\nResults for text2:")
print(f"Real substring: BM={t2_bm:.5f}, KMP={t2_kmp:.5f}, RK={t2_rk:.5f}")
print(
    f"Fake substring: BM={t2_bm_fake:.5f}, KMP={t2_kmp_fake:.5f}, RK={t2_rk_fake:.5f}"
)
