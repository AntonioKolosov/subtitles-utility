## Subtitles Utility

### File system structure      
├── main.py  
├── .gitignore  
├── README.md  

#### 1. Convert from subtitle format to the content format with the next commant:
```bash
$:python main.py path/to/input/file path/to/output/file
```

#### 2. Remove docer image 
```bash
$:docker image rm antonioklsv/subtitles-utility-aarch64:1.0.0
```

#### 2. Manually build docer image aarch64 (x64 build via Github action) 
```bash
$:docker build --no-cache . --tag antonioklsv/subtitles-utility-aarch64:1.0.0
```

#### 3. Manually push docer image aarch64 to Docker Hub (x64 push via Github action) 
```bash
$:docker push antonioklsv/subtitles-utility-aarch64:1.0.0
```
