-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/eGvD1s
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "pub_rec_clean" (
    "MLSNumber" varchar   NOT NULL UNIQUE,
    "Tax_ID" varchar   NOT NULL,
    "Address-truncated" varchar   NOT NULL,
    "PropertyCityState" varchar   NOT NULL,
    "Zip_Code" varchar   NOT NULL,
    "Zip4" varchar   NULL,
    "CarrierRoute" varchar   NULL,
    "PropDoNotMail" varchar   NULL,
    "OwnerNames" varchar   NULL,
    "OwnerLastName" varchar   NULL,
    "OwnerFirstName" varchar   NULL,
    "Owner2LastName" varchar   NULL,
    "Owner2FirstName" varchar   NULL,
    "Owner3LastName" varchar   NULL,
    "Owner3FirstName" varchar   NULL,
    "OwnerAddress" varchar   NULL,
    "OwnerCityState" varchar   NULL,
    "OwnerZipCode" varchar   NULL,
    "OwnerZip4" varchar   NULL,
    "OwnerCarrierRoute" varchar   NULL,
    "OwnerOccupied" bool   NULL,
    "Municipality" varchar   NULL,
    "SubdivisionNeighborhood" varchar   NULL,
    "TaxIDAlt" varchar   NULL,
    "TaxMap" varchar   NULL,
    "Block" varchar   NULL,
    "Lot" varchar   NULL,
    "SchoolDistrict" varchar   NULL,
    "TaxYear" int   NULL,
    "AnnualTax" int   NULL,
    "CountyTax" int   NULL,
    "MunicipalTax" int   NULL,
    "SchoolTax" int   NULL,
    "TotalLandAsmt" int   NULL,
    "TotalBldgAsmt" int   NULL,
    "TaxableTotalAsmt" int   NULL,
    "DeedRecordDate" date   NULL,
    "SettleDate" date   NULL,
    "SaleAmt" int   NULL,
    "SaleType" varchar   NULL,
    "PropertyClass" varchar   NULL,
    "CondoYN" varchar   NULL,
    "LotFrontage" float   NULL,
    "LotDepth" float   NULL,
    "LotSqFt" int   NULL,
    "LotAcres" float   NULL,
    "LotShape" varchar   NULL,
    "Zoning" varchar   NULL,
    "BldgSqFtTotal" float   NULL,
    "Stories" float   NULL,
    "Bedrooms" float   NULL,
    "Exterior" varchar   NULL,
    "BsmtDesc" varchar   NULL,
    "FireplaceTotal" float   NULL,
    "GrgType" varchar   NULL,
    "HeatDelivery" varchar   NULL,
    "YearBuilt" varchar   NULL,
    "YearRemod" varchar   NULL,
    CONSTRAINT "pk_pub_rec_clean" PRIMARY KEY (
        "MLSNumber"
     )
);

CREATE TABLE "broker_data_clean" (
    "MLSNumber" varchar   NOT NULL,
    "Address" varchar   NOT NULL,
    "ListOfficeName" varchar   NOT NULL,
    "ListAgentName" varchar   NOT NULL,
    CONSTRAINT "pk_broker_data_clean" PRIMARY KEY (
        "MLSNumber"
     )
);

CREATE TABLE "id_table" (
    "MLSNumber" varchar   NOT NULL,
    "Address" varchar   NULL,
    "Category" varchar   NULL,
    "City" varchar   NULL,
    "State" varchar   NULL,
    "Zip_Code" varchar   NULL,
    "County" varchar   NULL,
    "MLSArea" varchar   NULL,
    "Subdivision" varchar   NULL,
    "School_District" varchar   NULL,
    "Schools-Elementary" varchar   NULL,
    "Schools-Middle" varchar   NULL,
    "Schools-HighSchool" varchar   NULL,
    CONSTRAINT "pk_id_table" PRIMARY KEY (
        "MLSNumber"
     )
);

CREATE TABLE "mortgage_data_clean" (
    "Tax_ID" varchar   NOT NULL,
    "Address" varchar   NOT NULL,
    "Lender" varchar   NULL,
    "Mort_Amt" float   NULL,
    "Mort_Type" varchar   NULL,
    "Mort_Int_Rate" float   NULL,
    "Mort_Term" varchar   NULL,
    "Mort_Record_Date" varchar   NULL,
    "Mort_Due_Date" varchar   NULL,
    "Mort_Date" varchar   NULL,
    CONSTRAINT "pk_mortgage_data_clean" PRIMARY KEY (
        "Tax_ID"
     )
);

CREATE TABLE "sales_data_clean" (
    "MLSNumber" varchar   NOT NULL,
    "Address" varchar   NOT NULL,
    "Status" varchar   NULL,
    "Sold_Price" float   NOT NULL,
    "Sold_Price_less_Concession" float   NOT NULL,
    "Orig_List_Price" float   NULL,
    "Current_List_Price" float   NULL,
    "Days_on_Market" float   NOT NULL,
    "Previous_Days_on_Market" float   NULL,
    "ListDate" date   NOT NULL,
    "StatusDate" date   NOT NULL,
    "Agreement_of_Sale_Date" date   NOT NULL,
    "SettledDate" date   NOT NULL,
    "Concessions_YN" varchar   NULL,
    "Concessions_Remarks" varchar   NULL,
    "SellerConcessionsAmount" float   NULL,
    "FinalFinancing" varchar   NULL,
    CONSTRAINT "pk_sales_data_clean" PRIMARY KEY (
        "MLSNumber"
     )
);

CREATE TABLE "prop_charac_clean" (
    "MLSNumber" varchar   NOT NULL,
    "Address" varchar   NULL,
    "BuildingName" varchar   NULL,
    "Ownership" varchar   NULL,
    "Senior_Community_YN" varchar   NULL,
    "Condo/Coop_Assoc_YN" varchar   NULL,
    "HOA_YN" varchar   NULL,
    "AssociationFee" varchar   NULL,
    "AssociationFeeFrequency" varchar   NULL,
    "Structure_Type" varchar   NULL,
    "Acres" float   NULL,
    "LotDimensions" varchar   NULL,
    "LotDescription" varchar   NULL,
    "FeeIncludes" varchar   NULL,
    "Age" float   NULL,
    "InteriorSqFt" float   NULL,
    "Interior_SqFt_Source" varchar   NULL,
    "AboveGradeSqFt" float   NULL,
    "BelowGradeSqFt" float   NULL,
    "PropertyCondition" varchar   NULL,
    "Bedrooms" float   NULL,
    "Baths" float   NULL,
    "BathsFull" float   NULL,
    "PartialBaths" float   NULL,
    "Design" varchar   NULL,
    "Style" varchar   NULL,
    "NumberofStories" varchar   NULL,
    "RoomCount" float   NULL,
    "InteriorFeatures" varchar   NULL,
    "Flooring" varchar   NULL,
    "Central_Air_YN" varchar   NULL,
    "Cooling" varchar   NULL,
    "PrimaryHeat" varchar   NULL,
    "HeatDelivery" varchar   NULL,
    "HotWater" varchar   NULL,
    "ElectricalSystem" varchar   NULL,
    "Water" varchar   NULL,
    "Sewer" varchar   NULL,
    "Fireplace_YN" varchar   NULL,
    "FireplaceCount" float   NULL,
    "FireplaceFeatures" varchar   NULL,
    "KitchenAppliancesFeatures" varchar   NULL,
    "CookingFuel" varchar   NULL,
    "LaundryHookUps" varchar   NULL,
    "Basement_YN" varchar   NULL,
    "BasementType" varchar   NULL,
    "BasementDescription" varchar   NULL,
    "BasementFootprintPct" float   NULL,
    "BasementFinishedPct" float   NULL,
    "Garage_YN" varchar   NULL,
    "GarageSpaces" float   NULL,
    "GarageFeatures" varchar   NULL,
    "Parking" varchar   NULL,
    "ExteriorFeatures" varchar   NULL,
    "ExteriorMaterial" varchar   NULL,
    "Main_Roof" varchar   NULL,
    "Foundation" varchar   NULL,
    "PorchDeck" varchar   NULL,
    "SwimmingPoolType" varchar   NULL,
    CONSTRAINT "pk_prop_charac_clean" PRIMARY KEY (
        "MLSNumber"
     )
);

CREATE TABLE "lat_lng_clean" (
    "MLSNumber" varchar   NOT NULL,
    "address_new" varchar NULL,
    "lat" float   NULL,
    "lng" float   NULL,
    CONSTRAINT "pk_lat_lng_clean" PRIMARY KEY (
        "MLSNumber"
     )
);

ALTER TABLE "pub_rec_clean" ADD CONSTRAINT "fk_pub_rec_clean_MLSNumber" FOREIGN KEY("MLSNumber")
REFERENCES "id_table" ("MLSNumber");

ALTER TABLE "broker_data_clean" ADD CONSTRAINT "fk_broker_data_clean_MLSNumber" FOREIGN KEY("MLSNumber")
REFERENCES "id_table" ("MLSNumber");

ALTER TABLE "sales_data_clean" ADD CONSTRAINT "fk_sales_data_clean_MLSNumber" FOREIGN KEY("MLSNumber")
REFERENCES "id_table" ("MLSNumber");

ALTER TABLE "prop_charac_clean" ADD CONSTRAINT "fk_prop_charac_clean_MLSNumber" FOREIGN KEY("MLSNumber")
REFERENCES "id_table" ("MLSNumber");

ALTER TABLE "lat_lng_clean" ADD CONSTRAINT "fk_lat_lng_clean_MLSNumber" FOREIGN KEY("MLSNumber")
REFERENCES "id_table" ("MLSNumber");



