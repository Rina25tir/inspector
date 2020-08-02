# the case of the simplified table where p=1p(1)1, q=1q(1)1 and c1=0. Take only c2.
# with constraint term (2(p1+q1)-2)^2

from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector
from dimod import BinaryQuadraticModel


#sampler_manual = DWaveSampler(solver={'qpu': True})
sampler_auto = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
# Set Q for the problem QUBO
linear = {('s1', 's1'): -28/2, ('s2', 's2'): -28/2, ('s3', 's3'): -4/2,
('s4', 's4'): 40/2, ('s5', 's5'): 60/2  }

quadratic = {('s1', 's2'): 183/2, ('s1', 's3'): -2/2, ('s1', 's4'): -3/2, ('s1', 's5'): 48/2,
('s2', 's3'): -2/2, ('s2', 's4'): -3/2, ('s2', 's5'): 48/2, 
('s3', 's4'): 16/2, ('s3', 's5'): -4/2, ('s4', 's5'): -8/2}

#60*s5 - 28*s2 - 4*s3 - 8*s4 - 28*s1 + 183*s1*s2 - 2*s1*s3 - 3*s1*s4 - 2*s2*s3 + 48*s1*s5
 #- 3*s2*s4 + 48*s2*s5 + 16*s3*s4 - 4*s3*s5 - 8*s4*s5 + 148


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