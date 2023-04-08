import parmed as pmd

host_dict = {"OAH":"oa","OAMe":"oam"}

filetoconvert = "b.gro"
#import nglview as nv
from pathlib import Path
cwd = Path().absolute()
print(cwd)
import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      #print(os.path.join(root, name))
      #print(os.path.dirname(root))
      #print(os.path.basename(root))
      #print(os.path.basename(name))
      if(os.path.basename(root).split("_")[0] in host_dict and os.path.basename(root).split("_")[1]!="alone"):
            if(os.path.basename(name) == filetoconvert):
                  print(os.path.basename(root))
                  print(os.path.basename(name))
                  components = os.path.basename(root).split("_")
                  filepath = Path("host-"+host_dict[components[0]]+components[1].replace("G", "-lda-guest-")+".pdb")
                  print(cwd/filepath)
                  amber = pmd.load_file(os.path.join(root, name))
                  amber.save(str(filepath), overwrite=True)
   #for name in dirs:
   #   print(os.path.join(root, name))
#amber = pmd.load_file('/home/greg/Desktop/GHOAT.py/GHOAT/equil/guest-5/full.prmtop', '/home/greg/Desktop/GHOAT.py/GHOAT/equil/guest-5/full.inpcrd')
#amber.save('../output/CHARMM/restraints/host_restraints.pdb', overwrite=True)
