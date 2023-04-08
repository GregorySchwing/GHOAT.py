import parmed as pmd
from parmed.gromacs import GromacsTopologyFile, GromacsGroFile
host_dict = {"OAH":"oa","OAMe":"oam"}
host_oldresname_dict = {"OAH":"CLP","OAMe":"OCB"}
host_newresname_dict = {"OAH":"OAH","OAMe":"OAM"}
hgcoords = "b.gro"
hcoords = "nolig.gro"
topol = "topol.top"
#import nglview as nv
from pathlib import Path
cwd = Path().absolute()
print(cwd)
import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if(os.path.basename(root).split("_")[0] in host_dict and os.path.basename(root).split("_")[1]!="alone"):
            if(os.path.basename(name) == hgcoords):
                  print(os.path.basename(root))
                  print(os.path.basename(name))
                  components = os.path.basename(root).split("_")
                  filepath = Path(components[1].replace("G", "lda-guest-")+".mol2")
                  print(cwd/filepath)
                  print(os.path.join(root, topol))
                  print(os.path.join(root, hgcoords))

                  gmx_top = GromacsTopologyFile(os.path.join(root, topol))

                  gmx_gro = GromacsGroFile.parse(os.path.join(root, hgcoords))

                  gmx_top.box = gmx_gro.box # Needed because .prmtop contains box info

                  gmx_top.positions = gmx_gro.positions
                  #amber = pmd.load_file(os.path.join(root, topol),os.path.join(root, coords))
                  guest = gmx_gro["(:MOL)"]
                  guest.save(str(cwd/filepath), overwrite=True)
      if(os.path.basename(root).split("_")[0] in host_dict and os.path.basename(root).split("_")[1]=="alone"):
            if(os.path.basename(name) == hcoords):
                  print(os.path.basename(root))
                  print(os.path.basename(name))
                  components = os.path.basename(root).split("_")
                  filepath = Path("host-"+host_dict[components[0]]+".mol2")
                  print(cwd/filepath)
                  print(os.path.join(root, topol))
                  print(os.path.join(root, hcoords))

                  gmx_top = GromacsTopologyFile(os.path.join(root, topol))

                  gmx_gro = GromacsGroFile.parse(os.path.join(root, hcoords))

                  gmx_top.box = gmx_gro.box # Needed because .prmtop contains box info

                  gmx_top.positions = gmx_gro.positions
                  #amber = pmd.load_file(os.path.join(root, topol),os.path.join(root, coords))
                  host = gmx_gro["(:{})".format(host_oldresname_dict[components[0]])]
                  for res in host.residues:
                        if res.name == host_oldresname_dict[components[0]]:
                              res.name = host_newresname_dict[components[0]]
                  host.save(str(cwd/filepath), overwrite=True)
   #for name in dirs:
   #   print(os.path.join(root, name))
#amber = pmd.load_file('/home/greg/Desktop/GHOAT.py/GHOAT/equil/guest-5/full.prmtop', '/home/greg/Desktop/GHOAT.py/GHOAT/equil/guest-5/full.inpcrd')
#amber.save('../output/CHARMM/restraints/host_restraints.pdb', overwrite=True)
