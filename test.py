import netCDF4 as nc

ds = nc.Dataset(r"C:\Users\f.ekinci\Downloads\va\va.nc", "r", format="NETCDF4")
#print(ds["lat_bnds"].variables)
print(ds["lat_bnds"].type)


# print(ds.dimensions)

# for dim in ds.dimensions.values():
#     print(dim)



            # for key, value in self.ds.dimensions.items():
            # self.label.setText(str(value).split(",")[1])
            # print(str(value).split(",")[1])