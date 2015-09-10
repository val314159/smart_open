import os, sys, stat
from smart_open import smart_open

def recursive_upload(remotefs,localfs='.',tab='',policy='public-read'):
    for dirname in os.listdir(localfs):
        if dirname.startswith('.'):
            continue
        fulllocalname  = os.path.join(localfs, dirname)
        fullremotename = os.path.join(remotefs,dirname)
        if os.path.isdir(fulllocalname):
            recursive_upload( fullremotename, fulllocalname, '- '+tab )
        else:
            fr = smart_open(fulllocalname, 'rb')
            fw = smart_open(fullremotename,'wb',policy=policy)
            try:
                for line in fr:
                    fw.write( line )
            finally:
                fr.close()
                fw.close()
                pass
            pass
        pass
    pass

def main(): recursive_upload( *sys.argv[1:] )

if __name__=='__main__': main()
