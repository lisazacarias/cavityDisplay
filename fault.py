class Fault:
    def __init__(self, cavity, rowData):
        self.severity = rowData[3]
        self.tlc = rowData[4]
        self.pv = rowData[6].format(cavity.name, cavity.parent.name, cavity.grandparent.name)

    def __gt__(self, other):
        return self.severity > other.severity

    def isFaulted(self):
        pass

    def writeToPVs(self):
        pass

csvRowList = []
faults = []
reader = csvReader("faults.csv")
for row in reader:
    csvRowList.append(row)
    faults.append(Fault(row))

# csvRowList = [[0,1,"sdadad", "${cavitynumber}"],[]]

class Cavity:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.faults = []
        self.grandparent = self.parent.parent

        # for fault in fault:
        #     self.faults.append(Fault(self, rowData))

class Linac:
    def __init__(self, name, cryomodules):
        self.name = name
        self.cryomodules = []
        for cryomodule in cryomodules:
            self.cryomodules.append(Cryomodule(cryomodule, self))

class Cryomodule:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.cavities = []
        for i in range(1, 9):
            self.cavities.append(Cavity(i, self))

linacs = [Linac("L0B", ["01"]), Linac("L1B", ["02", "03", "H1", "H2"])]


"ACCL:${LINAC}:${CRYOMODULE}${cavity}:SSA_LTCH"






