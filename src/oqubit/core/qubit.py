import numpy as np
class Qubit():
    """
Qubit represents a single-qubit quantum state of the form

    |ψ⟩ = α|0⟩ + β|1⟩

where alpha and beta are the probability amplitudes.
The normalize parameter determines whether the state is
normalized during initialization.
"""
    def __init__(self,alpha=1,beta=0,normalize=True):
        self.alpha=complex(alpha)
        self.beta=complex(beta)
        self.normalize=normalize
        if (normalize==True):
            self._normalize()
    def _normalize(self):
        norm = np.sqrt(abs(self.alpha) ** 2 +abs(self.beta) ** 2)
        if np.isclose(norm, 0):
            raise ValueError("Cannot normalize zero state.")
        self.alpha /= norm
        self.beta /= norm
    @classmethod
    def i(cls):
        return cls(1 / np.sqrt(2), 1j / np.sqrt(2))
    @classmethod
    def minus_i(cls):
        return cls(1 / np.sqrt(2), -1j / np.sqrt(2))
    @classmethod
    def plus(cls):
        return cls(1/np.sqrt(2), 1/np.sqrt(2))
    @classmethod
    def minus(cls):
        return cls(1/np.sqrt(2),-1/np.sqrt(2))
    @classmethod
    def zero(cls):
        return cls(1,0)
    @classmethod
    def one(cls):
        return cls(0,1)
    @property
    def state(self):
        return np.array([self.alpha,self.beta],dtype=complex)
    @property 
    def prob_0(self):
        norm = np.sqrt(abs(self.alpha) ** 2 +abs(self.beta) ** 2)
        if np.isclose(norm, 0):
            raise ValueError("Cannot normalize zero state.")
        alpha=abs(self.alpha)/norm
        return (alpha)**2
    @property
    def prob_1(self):
        norm = np.sqrt(abs(self.alpha) ** 2 +abs(self.beta) ** 2)
        if np.isclose(norm, 0):
            raise ValueError("Cannot normalize zero state.")
        beta=abs(self.beta)/norm
        return (beta)**2
    def __repr__(self):
        return f"Qubit:\t{self.alpha} |0\u27E9 \t {self.beta}|1\u27E9"
__all__=["Qubit"]