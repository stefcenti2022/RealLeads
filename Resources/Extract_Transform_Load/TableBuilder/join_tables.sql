
-- 1) Retrieve the data columns from the lat_lng_clean table.
SELECT l.MLSNumber,
    l.address_new,
    l.lat,
    l.lng,
-- 2) Retrieve the Zip_code and MLS Area from the id_table.	
    i.MLSNumber,
	i.Zip_Code,
	i.MLSArea
-- 3) Create a new table using the INTO clause.	
INTO expanded_lat_lng
FROM lat_lng_clean as l
-- 4) Join both tables on the primary key.
INNER JOIN id_table as i
ON l.MLSNumber = i.MLSNumber;


SELECT * FROM expanded_lat_lng;

