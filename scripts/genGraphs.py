#!/usr/bin/env python3

import linkStats as ls

file = "../parsedData/plvStats.txt"

ls.FPvsVP(file)
ls.ASvsVPvsCS(file)
ls.TPvsVPvsCS(file)
