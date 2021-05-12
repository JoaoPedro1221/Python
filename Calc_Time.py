import time
import timeit


alguma_funcao()


inicio = timeit.default_timer()
alguma_funcao()
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
