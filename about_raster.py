#!/usr/bin/python3
import sys
import os.path

import pyproj


try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERROR: cannot find GDAL/OGR modules')

# Enable GDAL/OGR exceptions
gdal.UseExceptions()


def rule_name(file):
    base = os.path.dirname(file)
    dirs=base.split('/')
    fname=os.path.basename(file).split('.')[0]
    return '{}_{}_{}'.format(dirs[-2],dirs[-1],fname)

class TiffHelper(object):
    def __init__(self,src_tif):
        try:
            self.ds = gdal.Open(src_tif)
        except RuntimeError as e:
            print('Open tiff file RuntimeError {}'.format(e))
            sys.exit(1)

    def get_epsg(self):
        try:
            proj_str=self.ds.GetProjection()
            if proj_str == '':
                return None
            else:
                cs = pyproj.CRS.from_string(proj_str)
                return cs.to_epsg()
        except RuntimeError as e:
            print('Get CRS error: {}'.format(e))

    def size_and_bbox(self):
        x = self.ds.RasterXSize
        y = self.ds.RasterYSize
        geoTrans=self.ds.GetGeoTransform() #(15517711.929215858, 0.18413328650671884, 0.0, 4218729.141664863, 0.0, -0.18413328650671884)

        pixelWidth=geoTrans[1]
        pixelHeigth=geoTrans[5]

        bbox0=geoTrans[0]
        bbox3=geoTrans[3]

        bbox1=bbox3 + pixelHeigth * y
        bbox2=bbox0 + pixelWidth * x

        bbox0,bbox1,bbox2,bbox3=round(bbox0,9),round(bbox1,9),round(bbox2,9),round(bbox3,9)
        return x,y,(bbox0,bbox1,bbox2,bbox3)


if __name__ == '__main__':
    #src_tif = '/home/upload/30169/h28mini/02.tif'
    src_tif='/home/tony/data/H30/A014.tif'
    if len(sys.argv)>1:
        src_tif = sys.argv[1]

    parent=os.path.basename(os.path.dirname(src_tif))
    basename=os.path.basename(src_tif)
    # name = rule_name(src_tif)
    origin_tiff='{}/{}'.format(parent,basename)
    info = {'tiff': origin_tiff, 'parent':parent}

    tiff_helper = TiffHelper(src_tif)
    srcSRS = tiff_helper.get_epsg()
    print("srcSRS={}".format(srcSRS))
    info['origin_srs'] = srcSRS
    info['sizex'], info['sizey'], info['bbox'] = tiff_helper.size_and_bbox()
    print(info)
