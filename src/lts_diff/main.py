#!/usr/bin/python3
# Author: CDN (Diego) Damasceno
# Email: d.damasceno@cs.ru.nl
#
#    Implementation of the LTS_diff algorithm
# proposed by Walkinshaw and Bogdanov (2013)
# in the paper DOI:10.1145/2430545.2430549

import sys
import networkx as nx

def _computeScores(ref, updt, K):
    return None

def _identifyLandmaks(pairsToScore, ref, updt, T, R):
    return None

def _surrounding(kPairs, ref, updt):
    return None

def _removeConflicts(nPairs, checked):
    return None

def _pickHighest(nPairs, pairsToScore, ref, updt):
    return None

def ltsdiff(ref, updt, K=0.5, T=0.5, R=1.4):
    # See https://doi.org/10.1145/2430545.2430549 (Algorithm 1)
    # Line 1 @ Algorithm 1
    pairsToScore = _computeScores(ref, updt, K)
    print(f"States pair scores: {pairsToScore}")

    # Line 2 - 5 @ Algorithm 1
    kPairs = _identifyLandmaks(pairsToScore, ref, updt, T, R)
    print(f"Landmarks found: {kPairs}");
    # kPairs.forEach(pair ->System.out.print("\t" + pair.get(0) + "," + pair.get(1)));

    # Line 6 @ Algorithm 1
    nPairs = _surrounding(kPairs, ref, updt)
    checked = dict()
    # checked.put(0, new LinkedHashSet <> ()); checked.put(1, new LinkedHashSet <> ());
    # for (List < Integer > list : kPairs):
    #     checked.get(0).add(list.get(0))
    _removeConflicts(nPairs, checked);

    # Line 7-14 @ Algorithm 1
    while not nPairs.isEmpty():
        while not nPairs.isEmpty():
            # Line 9 @ Algorithm 1
            _ab = _pickHighest(nPairs, pairsToScore, ref, updt)
            print(f"Highest state pair found: {_ab.get(0)},{_ab.get(1)}")

            # Line 10 @ Algorithm 1
            kPairs.add(_ab)
            checked.get(0).add(_ab.get(0))
            checked.get(1).add(_ab.get(1))

            # Line 11 @ Algorithm 1
            _removeConflicts(nPairs, checked)

        # Line 13 @ Algorithm 1
        nPairs = _surrounding(kPairs, ref, updt)
        _removeConflicts(nPairs, checked)
    return kPairs

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv)<2: raise Exception(f'LTS_Diff requires two .dot files')

    f_dot1 = sys.argv[1]
    f_dot2 = sys.argv[2]

    print(f_dot1,f_dot2)

    m1 = nx.drawing.nx_pydot.read_dot(f_dot1)
    m2 = nx.drawing.nx_pydot.read_dot(f_dot2)

    ltsdiff(m1,m2)
    print(m1,m2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
