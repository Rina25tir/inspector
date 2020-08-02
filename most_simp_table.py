#Here we consider x=(2*s-1) 
# and the case of the simplified table where p=1p(1)1, q=1q(1)1 and c1=0. Take only c2.

from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector
from dimod import BinaryQuadraticModel


#sampler_manual = DWaveSampler(solver={'qpu': True})
sampler_auto = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
# Set Q for the problem QUBO
linear = {('s1', 's1'): 5/2, ('s2', 's2'): 5/2}

quadratic = {('s1', 's2'): 199/2}

#5*s1 + 5*s2 + 199*s1*s2

#
Q = dict(linear)
Q.update(quadratic)

#bqm = BinaryQuadraticModel.from_qubo(Q, offset=-103/2)
sampler = EmbeddingComposite(DWaveSampler())

# Minor-embed and sample 1000 times on a default D-Wave system
#sampleset=sampler.sample(bqm, num_reads=1000)
sampleset = sampler_auto.sample_ising(linear, quadratic, num_reads=10000)
#sampleset = sampler_manual.sample_qubo(Q, num_reads=1000)
print(sampleset)
dwave.inspector.show(sampleset)