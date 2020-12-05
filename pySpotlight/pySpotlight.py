if __name__ == '__main__':
    # Python has an OS module to help interact with the system.
    import os

    # Get path to Windows Spotlight folder.
    spotlight = os.environ['USERPROFILE'] + r'\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_' \
                                            r'cw5n1h2txyewy\LocalState\Assets'
    # Get path to desktop.
    # To avoid having to hardcode \ in future for different operating systems:
    # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    desktopfolder = os.environ['USERPROFILE'] + r'\Desktop\Spotlight'

    # distutils.dir_util is for manipulating directories. copy_tree can copy everything in a directory
    # to another target directory. If the target doesn't exist, it is created.
    from distutils.dir_util import copy_tree
    copy_tree(spotlight, desktopfolder)

    # Use os.rename to attach a new extension that will let us view Spotlight images. os.path.splitext() is
    # not necessary because these files do not come with file extensions.
    # Change working directory to allow Python to easily find the file to change.
    # Use os.listdir() to tell Python this is a folder and not a string we want to iterate over.
    # If the file is big enough to be a Spotlight image, add the extension so we can view it. Otherwise,
    # delete the file.
    os.chdir(desktopfolder)
    for file in os.listdir(desktopfolder):
        if (os.path.getsize(file) / 1000) > 500:
            os.rename(file, file + ".png")
        else:
            os.remove(file)
