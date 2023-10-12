import itertools

houses = ["rot", "grün", "weiß", "gelb", "blau"]
nationalities = ["Norweger", "Brite", "Schwede", "Däne", "Deutscher"]
drinks = ["Wasser", "Tee", "Milch", "Kaffee", "Bier"]
cigarettes = ["Dunhill", "Rothmanns", "Pall Mall", "Marlboro", "Winfield"]
pets = ["Hund", "Vogel", "Katze", "Pferd", "Fisch"]


house_permutation = [x for x in itertools.permutations(houses)]
nationalities_permutation = [x for x in itertools.permutations(nationalities)]
drinks_permutation = [x for x in itertools.permutations(drinks)]
cigarettes_permutation = [x for x in itertools.permutations(cigarettes)]
pets_permutation = [x for x in itertools.permutations(pets)]

for nations in nationalities_permutation:
    if nations[0] == "Norweger":
        for houses in house_permutation:
            if (
                houses[nations.index("Brite")] == "rot"
                and houses[houses.index("grün") - 1] == "weiß"
                and houses[nations.index("Norweger") + 1] == "blau"
            ):
                for drinks in drinks_permutation:
                    if (
                        drinks[nations.index("Däne")] == "Tee"
                        and drinks[houses.index("grün")] == "Kaffee"
                        and drinks[2] == "Milch"
                    ):
                        for cigarettes in cigarettes_permutation:
                            try:
                                if (
                                    cigarettes[houses.index("gelb")] == "Dunhill"
                                    and drinks[cigarettes.index("Winfield")] == "Bier"
                                    and cigarettes[nations.index("Deutscher")]
                                    == "Rothmanns"
                                    and (
                                        drinks[cigarettes.index("Marlboro") - 1]
                                        == "Wasser"
                                        or drinks[cigarettes.index("Marlboro") + 1]
                                        == "Wasser"
                                    )
                                ):
                                    for pets in pets_permutation:
                                        try:
                                            if (
                                                pets[nations.index("Schwede")] == "Hund"
                                                and pets[cigarettes.index("Pall Mall")]
                                                == "Vogel"
                                                and (
                                                    cigarettes[pets.index("Katze") - 1]
                                                    == "Marlboro"
                                                    or cigarettes[
                                                        pets.index("Katze") + 1
                                                    ]
                                                    == "Marlboro"
                                                )
                                                and (
                                                    cigarettes[pets.index("Pferd") - 1]
                                                    == "Dunhill"
                                                    or cigarettes[
                                                        pets.index("Pferd") + 1
                                                    ]
                                                    == "Dunhill"
                                                )
                                            ):
                                                print([f"{x:10}" for x in nations])
                                                print([f"{x:10}" for x in houses])
                                                print([f"{x:10}" for x in drinks])
                                                print([f"{x:10}" for x in cigarettes])
                                                print([f"{x:10}" for x in pets])
                                                print()
                                        except IndexError:
                                            continue
                            except IndexError:
                                continue

b = 1
