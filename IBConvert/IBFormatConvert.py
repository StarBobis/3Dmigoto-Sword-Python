import configparser
import struct

ib_file_path = "C:/Users/Administrator/Desktop/keqingventidesign/KeqingBody.ib"
read_ib_format = "DXGI_FORMAT_R16_UINT"
write_ib_format = "DXGI_FORMAT_R32_UINT"


def collect_ib(filename, offset):
    read_pack_sign = 'H'
    read_pack_stride = 2
    write_pack_sign = 'H'

    if read_ib_format == "DXGI_FORMAT_R16_UINT":
        read_pack_sign = 'H'
        read_pack_stride = 2

    if read_ib_format == "DXGI_FORMAT_R32_UINT":
        read_pack_sign = 'I'
        read_pack_stride = 4

    if write_ib_format == "DXGI_FORMAT_R16_UINT":
        write_pack_sign = 'H'

    if write_ib_format == "DXGI_FORMAT_R32_UINT":
        write_pack_sign = 'I'

    ib = bytearray()
    with open(filename, "rb") as f:
        data = f.read()
        data = bytearray(data)
        i = 0
        while i < len(data):
            ib += struct.pack(write_pack_sign, struct.unpack(read_pack_sign, data[i:i + read_pack_stride])[0] + offset)
            i += read_pack_stride
    return ib


if __name__ == "__main__":
    ib_bytearray = collect_ib(ib_file_path, 0)
    new_ib_file = open(ib_file_path + "_" + write_ib_format + ".ib", "wb")
    new_ib_file.write(ib_bytearray)
    new_ib_file.close()

