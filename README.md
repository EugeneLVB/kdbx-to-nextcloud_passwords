# kdbx-to-nextcloud_passwords
Convert kdbx to [Nextcloud Passwords](https://apps.nextcloud.com/apps/passwords) with saving folders.

## Steps
1. Make an export using [KeePasCX](https://keepassxc.org/download/).
2. Make sure the csv file does not contain unexpected newlines in comments.
3. Run

```shell
python3 convert.py keepassxc_export.csv
```
If all conditions are met, ```nextcloud_passwords_db.json``` will be created

4. Make import using ```Database backup``` format.  
  
<img src='https://user-images.githubusercontent.com/99425512/153473078-f4599d1e-0b1f-4d47-b6cf-cd93de06e340.png' width='250'>
