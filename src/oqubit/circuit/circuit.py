from ..core.operators import Gate
from ..core.statevector import StateVector
from ..core.qubit import Qubit
from ..measurement import measure, sample
from .instruction import Instruction
class Circuit:
    """
    Represents a quantum circuit.

    Parameters
    ----------
    num_qubits : int
        Number of qubits in the circuit.
    """
    def __init__(self, num_qubits):
        if not isinstance(num_qubits, int):
            raise TypeError("num_qubits must be an integer.")
        if num_qubits < 1:
            raise ValueError("num_qubits must be at least 1.")
        self.num_qubits = num_qubits
        self.instructions = []
    def _validate_qubit(self, qubit):
        if not isinstance(qubit, int):
            raise TypeError("Qubit index must be an integer.")
        if qubit < 0 or qubit >= self.num_qubits:
            raise IndexError(
                f"Qubit index {qubit} is out of range for "
                f"{self.num_qubits} qubits."
            )
    def _validate_qubits(self, qubits):
        for qubit in qubits:
            self._validate_qubit(qubit)
    def _add_instruction(self, gate, controls=None, targets=None):
        instruction = Instruction(
            gate=gate,
            controls=controls,
            targets=targets,
        )
        self._validate_qubits(instruction.qubits)
        self.instructions.append(instruction)
        return self
    def append(self, gate, controls=None, targets=None):
        return self._add_instruction(
            gate,
            controls=controls,
            targets=targets,
        )
    def x(self, qubit):
        from ..gates.single import X

        return self._add_instruction(
            X,
            targets=qubit,
        )

    def y(self, qubit):
        from ..gates.single import Y

        return self._add_instruction(
            Y,
            targets=qubit,
        )

    def z(self, qubit):
        from ..gates.single import Z

        return self._add_instruction(
            Z,
            targets=qubit,
        )

    def h(self, qubit):
        from ..gates.single import H

        return self._add_instruction(
            H,
            targets=qubit,
        )

    def s(self, qubit):
        from ..gates.single import S

        return self._add_instruction(
            S,
            targets=qubit,
        )

    def t(self, qubit):
        from ..gates.single import T

        return self._add_instruction(
            T,
            targets=qubit,
        )

    def sx(self, qubit):
        from ..gates.single import SX

        return self._add_instruction(
            SX,
            targets=qubit,
        )
    def cx(self, control, target):
        from ..gates.controlled import CX

        return self._add_instruction(
            CX,
            controls=control,
            targets=target,
        )

    def cy(self, control, target):
        from ..gates.controlled import CY

        return self._add_instruction(
            CY,
            controls=control,
            targets=target,
        )

    def cz(self, control, target):
        from ..gates.controlled import CZ

        return self._add_instruction(
            CZ,
            controls=control,
            targets=target,
        )

    def ch(self, control, target):
        from ..gates.controlled import CH

        return self._add_instruction(
            CH,
            controls=control,
            targets=target,
        )

    def cs(self, control, target):
        from ..gates.controlled import CS

        return self._add_instruction(
            CS,
            controls=control,
            targets=target,
        )

    def ct(self, control, target):
        from ..gates.controlled import CT

        return self._add_instruction(
            CT,
            controls=control,
            targets=target,
        )

    def csx(self, control, target):
        from ..gates.controlled import CSX

        return self._add_instruction(
            CSX,
            controls=control,
            targets=target,
        )
    def swap(self, qubit1, qubit2):
        from ..gates.multi import SWAP

        return self._add_instruction(
            SWAP,
            targets=[qubit1, qubit2],
        )

    def iswap(self, qubit1, qubit2):
        from ..gates.multi import ISWAP

        return self._add_instruction(
            ISWAP,
            targets=[qubit1, qubit2],
        )

    def sqrt_swap(self, qubit1, qubit2):
        from ..gates.multi import SQRT_SWAP

        return self._add_instruction(
            SQRT_SWAP,
            targets=[qubit1, qubit2],
        )

    def ccx(self, control1, control2, target):
        from ..gates.multi import CCX

        return self._add_instruction(
            CCX,
            controls=[control1, control2],
            targets=target,
        )

    def cswap(self, control, target1, target2):
        from ..gates.multi import CSWAP

        return self._add_instruction(
            CSWAP,
            controls=control,
            targets=[target1, target2],
        )
    def initial_state(self):
        qubits = [
            Qubit.zero()
            for _ in range(self.num_qubits)
        ]

        return StateVector(qubits)

    def run(self, state=None):
        if state is None:
            state = self.initial_state()

        if not isinstance(state, StateVector):
            raise TypeError("state must be a StateVector.")

        if state.num_qubits != self.num_qubits:
            raise ValueError(
                f"Circuit requires {self.num_qubits} qubits, "
                f"but state contains {state.num_qubits}."
            )

        for instruction in self.instructions:
            state.apply(
                instruction.gate,
                controls=instruction.controls,
                targets=instruction.targets,
            )

        return state
    def measure(self, state=None, qubits=None):
        if state is None:
            state = self.run()

        return measure(
            state,
            qubits=qubits,
        )

    def sample(self, shots=1024, state=None, qubits=None):
        if state is None:
            state = self.run()

        return sample(
            state,
            shots=shots,
            qubits=qubits,
        )
    @property
    def depth(self):
        return len(self.instructions)
    @property
    def notation(self):
        return self.run().notation
    @property
    def size(self):
        return len(self.instructions)
    def clear(self):
        self.instructions.clear()
        return self
    def __repr__(self):
        return (
            f"Circuit("
            f"num_qubits={self.num_qubits}, "
            f"instructions={len(self.instructions)})"
        )
    def __len__(self):
        return len(self.instructions)
    def __str__(self):
        return "\n".join(
            str(instruction)
            for instruction in self.instructions
        )
__all__ = ["Circuit"]