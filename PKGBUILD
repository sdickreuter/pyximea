# Maintainer: Joe User <joe.user@example.com>

pkgname=ximea_camera
pkgver=1.0
pkgrel=1
pkgdesc="Ximea camera drivers"
depends=('libusb')
arch=('x86_64')
url="https://www.ximea.com/support/wiki/apis/XIMEA_Linux_Software_Package"
license=('GPL')
source=("http://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz")
md5sums=('d46a5100ccf8a35f2f8257b313f6ffe2')

build() {
        cd "$srcdir/package"
        ls
}

package() {
        cd "$srcdir/package"
        mkdir -p "$pkgdir"/usr/{include/m3api,lib{,/udev/rules.d/}}
        sed 's/plugdev/video/g' libs/libusb/99-ximea.rules > "$pkgdir"/usr/lib/udev/rules.d/99-ximea.rules
        cp -r include/* "$pkgdir"/usr/include/m3api/
        cp api/X64/libm3api.so.0 "$pkgdir"/usr/lib/libm3api.so.0.0.0
        cp api/X64/libm3api.so.2 "$pkgdir"/usr/lib/libm3api.so.2.0.0
        ln -snf /usr/lib/libm3api.so.2.0.0 "$pkgdir"/usr/lib/libm3api.so
}
