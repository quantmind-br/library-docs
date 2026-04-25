---
title: Cài đặt không tương tác
url: https://docs.bmad-method.org/vi-vn/how-to/non-interactive-installation/
source: sitemap
fetched_at: 2026-04-08T11:32:13.306390212-03:00
rendered_js: false
word_count: 810
summary: This document provides a comprehensive guide on how to install BMad using command-line flags, detailing available options for modules, tools, and core configuration settings. It also explains different installation modes suitable for automated pipelines and troubleshooting common setup errors.
tags:
    - command-line
    - bmad-installation
    - ci-cd
    - configuration-flags
    - project-setup
    - tutorial
category: guide
---

Sử dụng các cờ dòng lệnh để cài đặt BMad mà không cần tương tác. Cách này hữu ích cho:

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

- Triển khai tự động và pipeline CI/CD
- Cài đặt bằng script
- Cài đặt hàng loạt trên nhiều dự án
- Cài đặt nhanh với cấu hình đã biết trước

## Các cờ khả dụng

[Phần tiêu đề “Các cờ khả dụng”](#c%C3%A1c-c%E1%BB%9D-kh%E1%BA%A3-d%E1%BB%A5ng)

### Tùy chọn cài đặt

[Phần tiêu đề “Tùy chọn cài đặt”](#t%C3%B9y-ch%E1%BB%8Dn-c%C3%A0i-%C4%91%E1%BA%B7t)

CờMô tảVí dụ`--directory <path>`Thư mục cài đặt`--directory ~/projects/myapp``--modules <modules>`Danh sách ID module, cách nhau bởi dấu phẩy`--modules bmm,bmb``--tools <tools>`Danh sách ID công cụ/IDE, cách nhau bởi dấu phẩy (dùng `none` để bỏ qua)`--tools claude-code,cursor` hoặc `--tools none``--action <type>`Hành động cho bản cài đặt hiện có: `install` (mặc định), `update`, hoặc `quick-update``--action quick-update`

### Cấu hình cốt lõi

[Phần tiêu đề “Cấu hình cốt lõi”](#c%E1%BA%A5u-h%C3%ACnh-c%E1%BB%91t-l%C3%B5i)

CờMô tảMặc định`--user-name <name>`Tên để agent sử dụngTên người dùng hệ thống`--communication-language <lang>`Ngôn ngữ giao tiếp của agentTiếng Anh`--document-output-language <lang>`Ngôn ngữ đầu ra tài liệuTiếng Anh`--output-folder <path>`Đường dẫn thư mục output (xem quy tắc resolve bên dưới)`_bmad-output`

#### Quy tắc resolve đường dẫn output folder

[Phần tiêu đề “Quy tắc resolve đường dẫn output folder”](#quy-t%E1%BA%AFc-resolve-%C4%91%C6%B0%E1%BB%9Dng-d%E1%BA%ABn-output-folder)

Giá trị truyền vào `--output-folder` (hoặc nhập ở chế độ tương tác) sẽ được resolve theo các quy tắc sau:

Loại đầu vàoVí dụĐược resolve thànhĐường dẫn tương đối (mặc định)`_bmad-output``<project-root>/_bmad-output`Đường dẫn tương đối có traversal`../../shared-outputs`Đường dẫn tuyệt đối đã được chuẩn hóa, ví dụ `/Users/me/shared-outputs`Đường dẫn tuyệt đối`/Users/me/shared-outputs`Giữ nguyên như đã nhập, **không** thêm project root vào trước

Đường dẫn sau khi resolve là đường dẫn mà agent và workflow sẽ dùng lúc runtime để ghi file đầu ra. Việc dùng đường dẫn tuyệt đối hoặc đường dẫn tương đối có traversal cho phép bạn chuyển toàn bộ artifact sinh ra sang một thư mục nằm ngoài cây dự án, hữu ích với thư mục dùng chung hoặc cấu trúc monorepo.

CờMô tả`-y, --yes`Chấp nhận toàn bộ mặc định và bỏ qua prompt`-d, --debug`Bật output debug cho quá trình tạo manifest

Những ID module có thể dùng với cờ `--modules`:

- `bmm` - BMad Method Master
- `bmb` - BMad Builder

Kiểm tra [BMad registry](https://github.com/bmad-code-org) để xem các module ngoài được hỗ trợ.

Những ID công cụ có thể dùng với cờ `--tools`:

**Khuyến dùng:** `claude-code`, `cursor`

Chạy `npx bmad-method install` một lần ở chế độ tương tác để xem danh sách đầy đủ hiện tại của các công cụ được hỗ trợ, hoặc xem [cấu hình platform codes](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml).

## Các chế độ cài đặt

[Phần tiêu đề “Các chế độ cài đặt”](#c%C3%A1c-ch%E1%BA%BF-%C4%91%E1%BB%99-c%C3%A0i-%C4%91%E1%BA%B7t)

Chế độMô tảVí dụHoàn toàn không tương tácCung cấp đầy đủ cờ để bỏ qua tất cả prompt`npx bmad-method install --directory . --modules bmm --tools claude-code --yes`Bán tương tácCung cấp một số cờ, BMad hỏi thêm phần còn lại`npx bmad-method install --directory . --modules bmm`Chỉ dùng mặc địnhChấp nhận tất cả giá trị mặc định với `-y``npx bmad-method install --yes`Không cấu hình công cụBỏ qua cấu hình công cụ/IDE`npx bmad-method install --modules bmm --tools none`

### Cài đặt cho pipeline CI/CD

[Phần tiêu đề “Cài đặt cho pipeline CI/CD”](#c%C3%A0i-%C4%91%E1%BA%B7t-cho-pipeline-cicd)

```bash

#!/bin/bash
npxbmad-methodinstall\
--directory"${GITHUB_WORKSPACE}"\
--modulesbmm\
--toolsclaude-code\
--user-name"CI Bot"\
--communication-languageEnglish\
--document-output-languageEnglish\
--output-folder_bmad-output\
--yes
```

### Cập nhật bản cài đặt hiện có

[Phần tiêu đề “Cập nhật bản cài đặt hiện có”](#c%E1%BA%ADp-nh%E1%BA%ADt-b%E1%BA%A3n-c%C3%A0i-%C4%91%E1%BA%B7t-hi%E1%BB%87n-c%C3%B3)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionupdate\
--modulesbmm,bmb,custom-module
```

### Quick Update (giữ nguyên cài đặt)

[Phần tiêu đề “Quick Update (giữ nguyên cài đặt)”](#quick-update-gi%E1%BB%AF-nguy%C3%AAn-c%C3%A0i-%C4%91%E1%BA%B7t)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionquick-update
```

## Bạn nhận được gì

[Phần tiêu đề “Bạn nhận được gì”](#b%E1%BA%A1n-nh%E1%BA%ADn-%C4%91%C6%B0%E1%BB%A3c-g%C3%AC)

- Thư mục `_bmad/` đã được cấu hình đầy đủ trong dự án của bạn
- Agent và workflow đã được cấu hình theo module và công cụ bạn chọn
- Thư mục `_bmad-output/` để lưu các artifact được tạo

## Kiểm tra và xử lý lỗi

[Phần tiêu đề “Kiểm tra và xử lý lỗi”](#ki%E1%BB%83m-tra-v%C3%A0-x%E1%BB%AD-l%C3%BD-l%E1%BB%97i)

BMad sẽ kiểm tra tất cả các cờ được cung cấp:

- **Directory** - Phải là đường dẫn hợp lệ và có quyền ghi
- **Modules** - Cảnh báo nếu ID module không hợp lệ (nhưng không thất bại)
- **Tools** - Cảnh báo nếu ID công cụ không hợp lệ (nhưng không thất bại)
- **Action** - Phải là một trong: `install`, `update`, `quick-update`

Giá trị không hợp lệ sẽ dẫn đến một trong các trường hợp sau:

1. Hiện lỗi và thoát (với các tùy chọn quan trọng như directory)
2. Hiện cảnh báo và bỏ qua (với mục tùy chọn)
3. Quay lại hỏi interactive (với giá trị bắt buộc bị thiếu)

## Khắc phục sự cố

[Phần tiêu đề “Khắc phục sự cố”](#kh%E1%BA%AFc-ph%E1%BB%A5c-s%E1%BB%B1-c%E1%BB%91)

### Cài đặt thất bại với lỗi “Invalid directory”

[Phần tiêu đề “Cài đặt thất bại với lỗi “Invalid directory””](#c%C3%A0i-%C4%91%E1%BA%B7t-th%E1%BA%A5t-b%E1%BA%A1i-v%E1%BB%9Bi-l%E1%BB%97i-invalid-directory)

- Thư mục đích phải tồn tại (hoặc thư mục cha của nó phải tồn tại)
- Bạn cần quyền ghi
- Đường dẫn phải là tuyệt đối, hoặc tương đối đúng với thư mục hiện tại

### Không tìm thấy module

[Phần tiêu đề “Không tìm thấy module”](#kh%C3%B4ng-t%C3%ACm-th%E1%BA%A5y-module)

- Xác minh ID module có đúng không
- Module bên ngoài phải có sẵn trong registry