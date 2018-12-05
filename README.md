# ML_Project
## TODO
- [x] split dataset to 9 subdataset
- [x] get API dict
- [ ] get metric
- [x] get number of thread
- [x] get label 

## Method 
- Neural Network
- Decision Tree

## 提交格式
> 1.选手的结果文件包含9个字段：file_id(bigint)、和八个分类的预测概率prob0, prob1, prob2, prob3, prob4, prob5 ,prob6,prob7 (类型double，范围在[0,1]之间，精度保留小数点后5位，prob<=0.0我们会替换为1e-6，prob>=1.0我们会替换为1.0-1e-6)。选手必须保证每一行的|prob0+prob1+prob2+prob3+prob4+prob5+prob6+prob7-1.0|<1e-6，且将列名按如下顺序写入提交结果文件的第一行，作为表头：file_id,prob0,prob1,prob2,prob3,prob4,prob5,prob6,prob7。

## Test
'MessageBoxTimeoutW' is not in list

'MessageBoxTimeoutW' is not in list

'NtDeleteFile' is not in list

'InternetGetConnectedStateExA' is not in list

'InternetGetConnectedStateExA' is not in list

'InternetGetConnectedStateExA' is not in list

'InternetGetConnectedStateExA' is not in list

'InternetGetConnectedStateExA' is not in list

'InternetGetConnectedStateExA' is not in list

'TaskDialog' is not in list

'NtCreateUserProcess' is not in list

'MessageBoxTimeoutW' is not in list

'CreateDirectoryExW' is not in list

'CreateDirectoryExW' is not in list

'CreateDirectoryExW' is not in list

'CreateDirectoryExW' is not in list

## 合并
['CertOpenSystemStoreA', 'CertOpenSystemStoreW']
['CoCreateInstance', 'CoCreateInstanceEx']
['CopyFileA', 'CopyFileExW']
['CreateDirectoryExW', 'CreateDirectoryW']
['CreateRemoteThread', 'CreateRemoteThreadEx']
['CreateServiceA', 'CreateServiceW']
['CryptAcquireContextA', 'CryptAcquireContextW']
['DeleteUrlCacheEntryA', 'DeleteUrlCacheEntryW']
['DnsQuery_A', 'DnsQuery_W']
['DrawTextExA', 'DrawTextExW']
['EnumServicesStatusA', 'EnumServicesStatusW']
['EnumWindows', 'ExitWindowsEx']
['FindFirstFileExA', 'FindFirstFileExW']
['FindResourceA', 'FindResourceExA', 'FindResourceExW', 'FindResourceW']
['FindWindowA', 'FindWindowExA', 'FindWindowExW', 'FindWindowW']
['GetComputerNameA', 'GetComputerNameW']
['GetSystemDirectoryA', 'GetSystemDirectoryW']
['GetSystemWindowsDirectoryA', 'GetSystemWindowsDirectoryW']
['GetUserNameA', 'GetUserNameExA', 'GetUserNameExW', 'GetUserNameW']
['GlobalMemoryStatus', 'GlobalMemoryStatusEx']
['HttpOpenRequestA', 'HttpOpenRequestW']
['InternetConnectA', 'InternetConnectW']
['InternetCrackUrlA', 'InternetCrackUrlW']
['InternetGetConnectedState', 'InternetGetConnectedStateExW', 'InternetGetConnectedStateExA']
['InternetOpenUrlA', 'InternetOpenUrlW']
['LoadStringA', 'LoadStringW']
['MessageBoxTimeoutA', 'MessageBoxTimeoutW']
['NtOpenKey', 'NtOpenKeyEx']
['OpenSCManagerA', 'OpenSCManagerW']
['OpenServiceA', 'OpenServiceW']
['RegCreateKeyExA', 'RegCreateKeyExW']
['RegDeleteKeyA', 'RegDeleteKeyW']
['RegDeleteValueA', 'RegDeleteValueW']
['RegEnumKeyExA', 'RegEnumKeyExW', 'RegEnumKeyW']
['RegEnumValueA', 'RegEnumValueW']
['RegOpenKeyExA', 'RegOpenKeyExW']
['RegQueryInfoKeyA', 'RegQueryInfoKeyW']
['RegQueryValueExA', 'RegQueryValueExW']
['RegSetValueExA', 'RegSetValueExW']
['RemoveDirectoryA', 'RemoveDirectoryW']
['SendNotifyMessageA', 'SendNotifyMessageW']
['SetWindowsHookExA', 'SetWindowsHookExW']
['StartServiceA', 'StartServiceW']
['WSASocketA', 'WSASocketW']
['WriteConsoleA', 'WriteConsoleW']

