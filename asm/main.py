import numpy as np
from pyscf import gto, dft, scf
from pyscf.geomopt.geometric_solver import optimize
from pyscf.qsdopt.qsd_optimizer import QSD
import cirpy

class ActivationStrainModel:
    def __init__(self, basis, functional):
        self.basis = basis
        self.functional = functional

    def geometry_optimization(self, input_molecules):

        molecules = []  # Create PySCF objects

        for smiles in input_molecules:
            molecule = '\n'.join(cirpy.resolve(smiles, 'xyz').split('\n')[2:])
            print(molecule)
            molecule = gto.M(atom=molecule, basis=self.basis)
            mf = scf.RHF(molecule)
            # molecule = optimize(mf, maxsteps=100)
            molecule = mf.Gradients().optimizer(solver='geomeTRIC').kernel()
            molecules.append(molecule))

        return molecules

    def transition_state(self, molecules):


model = ActivationStrainModel('TZP', 'BLYP')

water = model.geometry_optimization(["H2O"])

print(water)
