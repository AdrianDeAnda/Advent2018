"""
NOT MY CODE.
Used to achieve the stars for the day, need to be redone with own code.
"""

import re
import math

inp_imm = """2667 units each with 9631 hit points (immune to cold; weak to radiation) with an attack that does 33 radiation damage at initiative 3
6889 units each with 7044 hit points (immune to cold, slashing) with an attack that does 8 cold damage at initiative 11
8030 units each with 8956 hit points (weak to bludgeoning) with an attack that does 8 fire damage at initiative 5
9278 units each with 9654 hit points (weak to slashing; immune to radiation) with an attack that does 10 radiation damage at initiative 9
3472 units each with 9606 hit points with an attack that does 26 cold damage at initiative 14
2971 units each with 4601 hit points (weak to cold, radiation) with an attack that does 14 fire damage at initiative 16
2455 units each with 6330 hit points (immune to slashing, radiation) with an attack that does 20 bludgeoning damage at initiative 20
1896 units each with 9385 hit points (weak to slashing, cold) with an attack that does 48 slashing damage at initiative 19
303 units each with 10428 hit points with an attack that does 328 radiation damage at initiative 13
4380 units each with 7040 hit points (weak to slashing) with an attack that does 16 slashing damage at initiative 8"""

inp_infection = """3122 units each with 52631 hit points (immune to slashing, cold) with an attack that does 29 slashing damage at initiative 2
4257 units each with 52159 hit points with an attack that does 22 bludgeoning damage at initiative 17
721 units each with 25099 hit points (weak to radiation, cold) with an attack that does 60 slashing damage at initiative 15
1772 units each with 44946 hit points (weak to cold) with an attack that does 49 slashing damage at initiative 7
886 units each with 22310 hit points (weak to slashing, radiation) with an attack that does 36 cold damage at initiative 12
2804 units each with 45281 hit points (weak to bludgeoning; immune to fire) with an attack that does 30 slashing damage at initiative 10
8739 units each with 43560 hit points (weak to bludgeoning; immune to radiation, slashing) with an attack that does 9 cold damage at initiative 1
1734 units each with 30384 hit points (weak to cold, bludgeoning) with an attack that does 34 cold damage at initiative 4
5525 units each with 14091 hit points (weak to cold) with an attack that does 4 bludgeoning damage at initiative 18
1975 units each with 15393 hit points with an attack that does 15 fire damage at initiative 6"""


class group:
    def __init__(
        self,
        n,
        hp_each,
        weaknesses,
        immunities,
        atk_dmg,
        atk_type,
        initiative,
        team,
    ):
        self.n = n
        self.hp_each = hp_each
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.atk_dmg = atk_dmg
        self.atk_type = atk_type
        self.initiative = initiative
        self.team = team

    def __repr__(self):
        return "group({!r})".format(self.__dict__)

    @property
    def eff_power(self):
        return self.n * self.atk_dmg

    def dmg_to(self, other):
        return self.eff_power * (
            0
            if self.atk_type in other.immunities
            else 2
            if self.atk_type in other.weaknesses
            else 1
        )


def parse(st, team, boost=0):
    res = []
    for i in st.split("\n"):
        g = re.match(
            r"(\d+) units each with (\d+) hit points (?:\((.*?)\) )?with an attack that does (\d+) (\S+) damage at initiative (\d+)",
            i,
        )
        n = int(g.group(1))
        hp = int(g.group(2))
        weaknesses = set()
        immunities = set()
        wi = g.group(3)
        if wi is not None:
            for cmp in wi.split("; "):
                if cmp.startswith("immune to "):
                    immunities |= set(cmp[len("immune to ") :].split(", "))
                elif cmp.startswith("weak to "):
                    weaknesses |= set(cmp[len("weak to ") :].split(", "))
        dmg = int(g.group(4))
        typ = g.group(5)
        initiative = int(g.group(6))
        res.append(
            group(
                n,
                hp,
                weaknesses,
                immunities,
                dmg + boost,
                typ,
                initiative,
                team,
            )
        )
    return res


def get_team(s):
    if s is None:
        return "stalemate"
    for i in s:
        return i.team


def run_combat(imm_inp, inf_inp, boost=0):
    immune_system = set(parse(imm_inp, "immune", boost))
    infection = set(parse(inf_inp, "infection"))
    while immune_system and infection:
        potential_combatants = immune_system | infection
        attacking = {}
        for combatant in sorted(
            immune_system | infection,
            key=lambda x: (x.eff_power, x.initiative),
            reverse=True,
        ):
            try:
                s = max(
                    (
                        x
                        for x in potential_combatants
                        if x.team != combatant.team and combatant.dmg_to(x) != 0
                    ),
                    key=lambda x: (
                        combatant.dmg_to(x),
                        x.eff_power,
                        x.initiative,
                    ),
                )
            except ValueError as e:
                attacking[combatant] = None
                continue
            potential_combatants.remove(s)
            attacking[combatant] = s
        did_damage = False
        for combatant in sorted(
            immune_system | infection, key=lambda x: x.initiative, reverse=True
        ):
            if combatant.n <= 0:
                continue
            atk = attacking[combatant]
            if atk is None:
                continue
            dmg = combatant.dmg_to(atk)
            n_dead = dmg // atk.hp_each
            if n_dead > 0:
                did_damage = True
            atk.n -= n_dead
            if atk.n <= 0:
                immune_system -= {atk}
                infection -= {atk}

        if not did_damage:
            return None
    winner = max(immune_system, infection, key=len)
    return winner


winner = run_combat(inp_imm, inp_infection)
print('Part 1:', sum(x.n for x in winner))

boost_min = 0
boost_max = 1
while get_team(run_combat(inp_imm, inp_infection, boost_max)) != 'immune':
    boost_max *= 2

import math
while boost_min != boost_max:
    pow = (boost_min + boost_max) // 2
    cr = run_combat(inp_imm, inp_infection, pow)
    res = get_team(cr)
    if res != 'immune':
        boost_min = math.ceil((boost_min + boost_max) / 2)
    else:
        boost_max = pow

print('Part 2:', sum(x.n for x in run_combat(inp_imm, inp_infection, boost_max)))
