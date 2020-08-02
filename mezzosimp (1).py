
# the case of the simplified table where p=1p(1)1, q=1q(1)1 and c1=0. Take only c2.
# with constraint term (2(p1+q1)-2)^2

from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector
from dimod import BinaryQuadraticModel


#sampler_manual = DWaveSampler(solver={'qpu': True})
sampler_auto = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
# Set Q for the problem QUBO
linear = {('s1', 's1'): -22/2, ('s2', 's2'): -22/2, ('s3', 's3'): 8/2,
('s4', 's4'): 40/2 }

quadratic = {('s1', 's2'): 191/2, ('s1', 's3'): -3/2, ('s1', 's4'): 32/2,
('s2', 's3'): -3/2, ('s2', 's4'): 32/2,
('s3', 's4'): -8/2}

#8*s3 - 22*s2 - 22*s1 + 40*s4 + 191*s1*s2 - 3*s1*s3 + 32*s1*s4 - 3*s2*s3 + 32*s2*s4 - 8*s3*s4 + 168


Q = dict(linear)
Q.update(quadratic)

#bqm = BinaryQuadraticModel.from_qubo(Q, offset=-103/2)
sampler = EmbeddingComposite(DWaveSampler())

# Minor-embed and sample 1000 times on a default D-Wave system
#sampleset=sampler.sample(bqm, num_reads=1000)
sampleset = sampler_auto.sample_ising(linear, quadratic, num_reads=1000)
#sampleset = sampler_manual.sample_qubo(Q, num_reads=1000)
print(sampleset)
dwave.inspector.show(sampleset)