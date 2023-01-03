# OIDv7 To VOC

Convert bounding box datasets of [Open Images Dataset v7](https://storage.googleapis.com/openimages/web/index.html) to VOC XML format.

## Installation

```sh
pip3 install oidv7-to-voc
```

## Usage

Once installed, you should be able to run it directly:

```sh
oidv7-to-voc -h
```

If your shell cannot find the command, try running it with:

```sh
python3 -m oidv7_to_voc -h
```

### CLI options

To start converting, you need at least a part of the images, the class names metadata *and* at least one of the boxes annotation CSV file:

![CSV files you need](https://user-images.githubusercontent.com/31200881/95124534-2902e600-0786-11eb-8702-4fbde2ef3aee.png)

```sh
oidv7-to-voc <annotation-file(s).csv>
             -d <class-names-file.csv> 
             --imgd <directory/to/your/images>
             --outd <your/output/diretory>
```

## About the Dataset

The Open Images V7 Dataset contains 600 classes with 1900000+ images. The images are hosted on AWS, and the CSV files can be [downloaded here](https://storage.googleapis.com/openimages/web/download.html).

To download it in full, you'll need 500+ GB of disk space. For downloading a part of the dataset only, I would recommend the [DmitryRyumin/OIDv6](https://github.com/DmitryRyumin/OIDv6) tool.

## Credit

This repo is forked from [chuangzhu/oidv6-to-voc](https://github.com/chuangzhu/oidv6-to-voc).
