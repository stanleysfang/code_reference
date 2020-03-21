
# Mount Disk to GCE instance
sudo lsblk
sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb
sudo mkdir -p /mnt/disks/staging
sudo mount -o discard,defaults /dev/sdb /mnt/disks/staging
sudo chmod a+w /mnt/disks/staging
sudo cp /etc/fstab /etc/fstab.backup
sudo blkid /dev/sdb
echo UUID=`sudo blkid -s UUID -o value /dev/sdb` /mnt/disks/staging ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
cat /etc/fstab
