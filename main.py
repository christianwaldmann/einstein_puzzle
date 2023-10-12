import itertools
from timeit import default_timer as timer
from datetime import timedelta


start = timer()


class NoWrap(list):
    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            return None
        else:
            return list.__getitem__(self, index)


def equals(first_list, first_list_element, second_list, second_list_element):
    return second_list[first_list.index(first_list_element)] == second_list_element


def left(first_list, first_list_element, second_list, second_list_element):
    return second_list[first_list.index(first_list_element) - 1] == second_list_element


def right(first_list, first_list_element, second_list, second_list_element):
    return second_list[first_list.index(first_list_element) + 1] == second_list_element


def next_to(first_list, first_list_element, second_list, second_list_element):
    return left(first_list, first_list_element, second_list, second_list_element) or right(
        first_list, first_list_element, second_list, second_list_element
    )


houses = ["rot", "grün", "weiß", "gelb", "blau"]
nationalities = ["Norweger", "Brite", "Schwede", "Däne", "Deutscher"]
drinks = ["Wasser", "Tee", "Milch", "Kaffee", "Bier"]
cigarettes = ["Dunhill", "Rothmanns", "Pall Mall", "Marlboro", "Winfield"]
pets = ["Hund", "Vogel", "Katze", "Pferd", "Fisch"]


house_permutation = [NoWrap(x) for x in itertools.permutations(houses)]
nationalities_permutation = [NoWrap(x) for x in itertools.permutations(nationalities)]
drinks_permutation = [NoWrap(x) for x in itertools.permutations(drinks)]
cigarettes_permutation = [NoWrap(x) for x in itertools.permutations(cigarettes)]
pets_permutation = [NoWrap(x) for x in itertools.permutations(pets)]


for nations in nationalities_permutation:
    if nations[0] == "Norweger":
        for houses in house_permutation:
            if (
                equals(nations, "Brite", houses, "rot")
                and left(houses, "grün", houses, "weiß")
                and right(nations, "Norweger", houses, "blau")
            ):
                for drinks in drinks_permutation:
                    if (
                        equals(nations, "Däne", drinks, "Tee")
                        and equals(houses, "grün", drinks, "Kaffee")
                        and drinks[2] == "Milch"
                    ):
                        for cigarettes in cigarettes_permutation:
                            if (
                                equals(houses, "gelb", cigarettes, "Dunhill")
                                and equals(cigarettes, "Winfield", drinks, "Bier")
                                and equals(nations, "Deutscher", cigarettes, "Rothmanns")
                                and next_to(cigarettes, "Marlboro", drinks, "Wasser")
                            ):
                                for pets in pets_permutation:
                                    if (
                                        equals(nations, "Schwede", pets, "Hund")
                                        and equals(cigarettes, "Pall Mall", pets, "Vogel")
                                        and next_to(pets, "Katze", cigarettes, "Marlboro")
                                        and next_to(pets, "Pferd", cigarettes, "Dunhill")
                                    ):
                                        print([f"{x:10}" for x in nations])
                                        print([f"{x:10}" for x in houses])
                                        print([f"{x:10}" for x in drinks])
                                        print([f"{x:10}" for x in cigarettes])
                                        print([f"{x:10}" for x in pets])
                                        print()


end = timer()
print(f"Time: {timedelta(seconds=end - start)}")
