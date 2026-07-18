from qiskit import QuantumCircuit, Aer, execute

def run_quantum_demo():
    """
    Demonstrates superposition and entanglement using a simple 2-qubit circuit.
    """
    # Create a quantum circuit with 2 qubits and 2 classical bits.
    # Qubits are initialized to the |0⟩ state by default.
    qc = QuantumCircuit(2, 2)

    print("Initial state: |00⟩")

    # Apply a Hadamard gate to the first qubit (qubit 0).
    # This puts qubit 0 into a superposition of |0⟩ and |1⟩.
    # The state becomes (1/√2)|00⟩ + (1/√2)|10⟩.
    qc.h(0)
    print("\nAfter Hadamard on qubit 0 (superposition):")
    print(qc.draw(output='text', fold=-1))

    # Apply a CNOT gate with qubit 0 as control and qubit 1 as target.
    # This creates an entangled Bell state: (1/√2)|00⟩ + (1/√2)|11⟩.
    # The qubits are now linked; measuring one instantly determines the other.
    qc.cx(0, 1)
    print("\nAfter CNOT (entanglement):")
    print(qc.draw(output='text', fold=-1))

    # Measure both qubits and map them to classical bits.
    # Due to superposition and entanglement, measuring will collapse the state
    # to either |00⟩ or |11⟩ with approximately 50% probability each.
    qc.measure([0, 1], [0, 1])
    print("\nAfter measurement:")
    print(qc.draw(output='text', fold=-1))

    # Select the QASM simulator backend for local execution.
    simulator = Aer.get_backend('qasm_simulator')

    # Execute the circuit on the simulator with 1024 shots.
    # 'shots' refers to the number of times the circuit is run to get statistics.
    job = execute(qc, simulator, shots=1024)

    # Retrieve the results from the job.
    result = job.result()

    # Get the measurement counts.
    counts = result.get_counts(qc)
    print("\nMeasurement results (counts):", counts)
    print("Expected: approximately 50% for '00' and 50% for '11'.")

if __name__ == "__main__":
    run_quantum_demo()
