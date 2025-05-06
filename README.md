# build-tencent-mars

该仓库用于编译`Tencent`的`mars`仓库`https://github.com/Tencent/mars`，并且将编译所得文件上传到`GitHub Actions`中。

## 1. 设置环境变量

```powershell
$env:MSVC_BIN_HOST64_PATH = "C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Tools\MSVC\14.43.34808\bin\Hostx64"
$env:MSVC_TOOLS_PATH = "C:\Program Files\Microsoft Visual Studio\2022\Enterprise\Common7\Tools"
```

## 2. 克隆仓库
```shell
git clone https://github.com/Tencent/mars.git
```

## 3. 编译

1. 将自身仓库目录下的`src_patches/CMakeLists.txt`覆盖替换`mars/mars/CMakeLists.txt`

2. 将自身仓库目录下的`src_patches/build_windows.py`覆盖替换`mars/mars/build_windows.py`

3. 将自身仓库目录下的`src_patches/positioning.hpp`覆盖替换`mars/mars/boost/iostreams/positioning.hpp`

4. 进入到目录`mars/mars`，运行命令`python .\build_windows.py --mars --config Release --incremental False`

5. 最后将`mars/mars/cmake_build/Windows/Windows.out/`文件夹下的所有文件以及子文件夹的内容压缩为`zip`，上传到`Actions`中。
