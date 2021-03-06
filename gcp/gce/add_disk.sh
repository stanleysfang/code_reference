
#### Mount Disk to GCE instance ####
# list attached disks
sudo lsblk

# The "mkfs" command will wipe the disk and format it.
sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb

# create mounting point
sudo mkdir -p /mnt/disks/staging
sudo mount -o discard,defaults /dev/sdb /mnt/disks/staging

# give write access
sudo chmod a+w /mnt/disks/staging

# automatically mount disk when opening terminal
sudo cp /etc/fstab /etc/fstab.backup
sudo blkid /dev/sdb
echo UUID=`sudo blkid -s UUID -o value /dev/sdb` /mnt/disks/staging ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
cat /etc/fstab
