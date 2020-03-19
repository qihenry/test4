# phantom to h5 file test!
from virtualscanner.server.simulation.bloch.phantom import *
import h5py

if __name__ == '__main__':
    p = makeCylindricalPhantom(dim=2,n=16,dir='z',loc=1,fov=0.24)
    print(p.type_params)
    print(p.T1map[8,8,:])
    print(p.T2map[8,8,:])
    print(p.PDmap[8,8,:])
    print(p.type_map[8,8])
    p.output_h5(output_folder='test_data', name='pht_h5_try')
    a = h5py.File('pht_h5_try.h5','a')
    print(a['sample'])

    print(a['sample']['data'][8,8,:,:])