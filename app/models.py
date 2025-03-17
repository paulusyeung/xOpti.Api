from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Double, Index, Integer, Numeric, PrimaryKeyConstraint, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
import decimal

class Base(DeclarativeBase):
    pass


class Add(Base):
    __tablename__ = 'Add'
    __table_args__ = (
        PrimaryKeyConstraint('AddCode', name='Add_pkey'),
        Index('Add_AddDescriptio', 'AddDescription')
    )

    AddCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    AddDescription: Mapped[Optional[str]] = mapped_column(String(40))


class BarCodePool(Base):
    __tablename__ = 'BarCodePool'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='BarCodePool_pkey'),
        Index('BarCodePool_ID', 'ID'),
        Index('BarCodePool_TxNumber', 'TxNumber')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    TxNumber: Mapped[str] = mapped_column(String(10))
    DateOfEntry: Mapped[datetime.datetime] = mapped_column(DateTime)
    SKU: Mapped[str] = mapped_column(String(13))
    Qty: Mapped[int] = mapped_column(Integer, server_default=text('0'))


class Branch(Base):
    __tablename__ = 'Branch'
    __table_args__ = (
        PrimaryKeyConstraint('BranchCode', name='Branch_pkey'),
        Index('Branch_PostalCode', 'PostalCode')
    )

    BranchCode: Mapped[str] = mapped_column(String(3), primary_key=True)
    BranchName: Mapped[str] = mapped_column(String(40))
    ContactPerson: Mapped[Optional[str]] = mapped_column(String(40))
    JobTitle: Mapped[Optional[str]] = mapped_column(String(30))
    Address1: Mapped[Optional[str]] = mapped_column(String(40))
    Address2: Mapped[Optional[str]] = mapped_column(String(40))
    City: Mapped[Optional[str]] = mapped_column(String(20))
    Province: Mapped[Optional[str]] = mapped_column(String(20))
    PostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    Country: Mapped[Optional[str]] = mapped_column(String(20))
    Phone: Mapped[Optional[str]] = mapped_column(String(13))
    Fax: Mapped[Optional[str]] = mapped_column(String(13))
    SummaryFlag: Mapped[Optional[bool]] = mapped_column(Boolean)


class BranchInventory(Base):
    __tablename__ = 'BranchInventory'
    __table_args__ = (
        PrimaryKeyConstraint('BranchCode', 'SKU', name='BranchInventory_pkey'),
        Index('BranchInventory_BranchCode', 'BranchCode'),
        Index('BranchInventory_SKU', 'SKU')
    )

    BranchCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    QtyOnHand: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class BranchSummary(Base):
    __tablename__ = 'BranchSummary'
    __table_args__ = (
        PrimaryKeyConstraint('BranchCode', 'Year', 'Month', 'FirstDateOfMonth', name='BranchSummary_pkey'),
        Index('BranchSummary_BranchCode', 'BranchCode'),
        Index('BranchSummary_FirstDateOfMonth', 'FirstDateOfMonth'),
        Index('BranchSummary_Month', 'Month'),
        Index('BranchSummary_Year', 'Year')
    )

    BranchCode: Mapped[str] = mapped_column(String(3), primary_key=True)
    Year: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    Month: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    FirstDateOfMonth: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    QtyBF: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtBF: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyCD: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtCD: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtySold: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    AmtCostOfGoodsSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyPurchased: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustIncr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustIncr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustDecr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustDecr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRejected: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRejected: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRestocked: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRestocked: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferIn: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferIn: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferOut: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferOut: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class Brand(Base):
    __tablename__ = 'Brand'
    __table_args__ = (
        PrimaryKeyConstraint('BrandCode', name='Brand_pkey'),
        Index('Brand_BrandDescription', 'BrandDescription')
    )

    BrandCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    BrandDescription: Mapped[Optional[str]] = mapped_column(String(40))


class Category(Base):
    __tablename__ = 'Category'
    __table_args__ = (
        PrimaryKeyConstraint('DepartmentCode', 'ClassCode', 'CategoryCode', name='Category_pkey'),
        Index('Category_CategoryCode', 'CategoryCode'),
        Index('Category_CategoryName', 'CategoryName'),
        Index('Category_ClassCode', 'ClassCode'),
        Index('Category_DepartmentCode', 'DepartmentCode')
    )

    DepartmentCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    ClassCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    CategoryCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    CostingMethod: Mapped[str] = mapped_column(String(1), server_default=text("'0'::character varying"))
    InventoryMethod: Mapped[str] = mapped_column(String(1), server_default=text("'0'::character varying"))
    TaxMethod: Mapped[str] = mapped_column(String(1), server_default=text("'0'::character varying"))
    CategoryName: Mapped[Optional[str]] = mapped_column(String(30))
    SummaryFlag: Mapped[Optional[bool]] = mapped_column(Boolean)


class CategorySummary(Base):
    __tablename__ = 'CategorySummary'
    __table_args__ = (
        PrimaryKeyConstraint('DepartmentCode', 'ClassCode', 'CategoryCode', 'Year', 'Month', 'FirstDateOfMonth', name='CategorySummary_pkey'),
        Index('CategorySummary_CategoryCode', 'CategoryCode'),
        Index('CategorySummary_ClassCode', 'ClassCode'),
        Index('CategorySummary_DepartmentCode', 'DepartmentCode'),
        Index('CategorySummary_FirstDateOfMonth', 'FirstDateOfMonth'),
        Index('CategorySummary_Month', 'Month'),
        Index('CategorySummary_Year', 'Year')
    )

    DepartmentCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    ClassCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    CategoryCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    Year: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    Month: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    FirstDateOfMonth: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    QtyBF: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtBF: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyCD: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtCD: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtySold: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    AmtCostOfGoodsSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyPurchased: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustedIncr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustedIncr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustedDecr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustedDecr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRejected: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRejected: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRestocked: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRestocked: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferIn: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferIn: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferOut: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferOut: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class City(Base):
    __tablename__ = 'City'
    __table_args__ = (
        PrimaryKeyConstraint('CityName', 'ProvinceCode', 'CountryCode', name='City_pkey'),
        UniqueConstraint('Code', name='City_Code_key'),
        Index('City_CityName', 'CityName'),
        Index('City_CityPhoneCode', 'CityPhoneCode'),
        Index('City_CountryCode', 'CountryCode'),
        Index('City_ProvinceCode', 'ProvinceCode')
    )

    Code: Mapped[int] = mapped_column(Integer)
    CityName: Mapped[str] = mapped_column(String(26), primary_key=True)
    ProvinceCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    CountryCode: Mapped[str] = mapped_column(String(3), primary_key=True)
    CityPhoneCode: Mapped[Optional[str]] = mapped_column(String(4))


class Class(Base):
    __tablename__ = 'Class'
    __table_args__ = (
        PrimaryKeyConstraint('Department', 'ClassCode', name='Class_pkey'),
        Index('Class_ClassCode', 'ClassCode'),
        Index('Class_ClassName', 'ClassName'),
        Index('Class_Department', 'Department')
    )

    Department: Mapped[str] = mapped_column(String(2), primary_key=True)
    ClassCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    ClassName: Mapped[Optional[str]] = mapped_column(String(30))
    SummaryFlag: Mapped[Optional[bool]] = mapped_column(Boolean)


class ClassSummary(Base):
    __tablename__ = 'ClassSummary'
    __table_args__ = (
        PrimaryKeyConstraint('DepartmentCode', 'ClassCode', 'Year', 'Month', 'FirstDateOfMonth', name='ClassSummary_pkey'),
        Index('ClassSummary_ClassCode', 'ClassCode'),
        Index('ClassSummary_FirstDateOfMonth', 'FirstDateOfMonth'),
        Index('ClassSummary_Month', 'Month'),
        Index('ClassSummary_Year', 'Year')
    )

    DepartmentCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    ClassCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    Year: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    Month: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    FirstDateOfMonth: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    QtyBF: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtBF: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyCD: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtCD: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtySold: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    AmtCostOfGoodsSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyPurchased: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustedIncr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustedIncr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustedDecr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustedDecr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRejected: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRejected: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRestocked: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRestocked: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferIn: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferIn: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferOut: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferOut: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class CostingMethod(Base):
    __tablename__ = 'CostingMethod'
    __table_args__ = (
        PrimaryKeyConstraint('CostingCode', name='CostingMethod_pkey'),
        UniqueConstraint('CostingName', name='CostingMethod_CostingName_key')
    )

    CostingCode: Mapped[str] = mapped_column(String(1), primary_key=True)
    CostingName: Mapped[str] = mapped_column(String(10))


class Country(Base):
    __tablename__ = 'Country'
    __table_args__ = (
        PrimaryKeyConstraint('CountryCode', name='Country_pkey'),
        UniqueConstraint('CountryName', name='Country_CountryName_key'),
        Index('Country_CountryCode1', 'CountryCode'),
        Index('Country_CountryPhoneCode', 'CountryPhoneCode')
    )

    CountryName: Mapped[str] = mapped_column(String(26))
    CountryCode: Mapped[str] = mapped_column(String(3), primary_key=True)
    CountryPhoneCode: Mapped[Optional[str]] = mapped_column(String(4))


class Customer(Base):
    __tablename__ = 'Customer'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='Customer_pkey'),
        Index('Customer_Birthday', 'Birthday'),
        Index('Customer_BizPostalCode', 'BizPostalCode'),
        Index('Customer_CountryLastname', 'HomeCountry', 'LastName'),
        Index('Customer_FirstName', 'FirstName'),
        Index('Customer_FullName', 'FullName'),
        Index('Customer_HomeCountry', 'HomeCountry'),
        Index('Customer_HomePhone', 'HomePhone'),
        Index('Customer_Initial', 'Initial'),
        Index('Customer_LastName', 'LastName'),
        Index('Customer_VIPCode', 'VIPCode'),
        Index('Customer_post_code', 'HomePostalCode')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    VIPCode: Mapped[Optional[str]] = mapped_column(String(16))
    FirstName: Mapped[Optional[str]] = mapped_column(String(20))
    Initial: Mapped[Optional[str]] = mapped_column(String(2))
    LastName: Mapped[Optional[str]] = mapped_column(String(20))
    FullName: Mapped[Optional[str]] = mapped_column(String(40))
    Salutation: Mapped[Optional[str]] = mapped_column(String(4))
    Birthday: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    HomeAddress: Mapped[Optional[str]] = mapped_column(String(128))
    HomeCity: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    HomeProvince: Mapped[Optional[str]] = mapped_column(String(2))
    HomePostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    HomeCountry: Mapped[Optional[str]] = mapped_column(String(3))
    HomePhone: Mapped[Optional[str]] = mapped_column(String(12))
    HomeFax: Mapped[Optional[str]] = mapped_column(String(12))
    Cellular: Mapped[Optional[str]] = mapped_column(String(15))
    Email: Mapped[Optional[str]] = mapped_column(String(128))
    BizCompanyName: Mapped[Optional[str]] = mapped_column(String(40))
    BizJobTitle: Mapped[Optional[str]] = mapped_column(String(20))
    BizAddress: Mapped[Optional[str]] = mapped_column(String(128))
    BizCity: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    BizProvince: Mapped[Optional[str]] = mapped_column(String(2))
    BizPostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    BizCountry: Mapped[Optional[str]] = mapped_column(String(3))
    BizPhone: Mapped[Optional[str]] = mapped_column(String(12))
    BizFax: Mapped[Optional[str]] = mapped_column(String(12))
    CreditLimit: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    PaymentTerms: Mapped[Optional[str]] = mapped_column(String(10))
    VIPMarkDownPct: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    SummaryFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    AccountingFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    Remarks: Mapped[Optional[str]] = mapped_column(Text)


class CustomerAccounts(Base):
    __tablename__ = 'CustomerAccounts'
    __table_args__ = (
        PrimaryKeyConstraint('CustomerID', name='CustomerAccounts_pkey'),
        Index('CustomerAccounts_CustJoinDate', 'CustomerID', 'JointDate'),
        Index('CustomerAccounts_CustLastPurchaseDate', 'CustomerID', 'LastPurchaseDate'),
        Index('CustomerAccounts_JointDate', 'JointDate'),
        Index('CustomerAccounts_LastPurchaseDate', 'LastPurchaseDate')
    )

    CustomerID: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    JointDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    TtlAmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TtlAmtRefund: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TtlAmtMrkdwnApplied: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TtlAmtCpnUsed: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    YTDAmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    YTDAmtRefund: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    YTDAmtMrkdwnApplied: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    YTDAmtCpnUsed: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    LastPurchaseDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class CustomerMedical(Base):
    __tablename__ = 'CustomerMedical'
    __table_args__ = (
        PrimaryKeyConstraint('CustomerID', name='CustomerMedical_pkey'),
        Index('CustomerMedical_CustCareCard', 'CustomerID', 'CareCardNo'),
        Index('CustomerMedical_CustInsDate', 'CustomerID', 'InsMaturityDate')
    )

    CustomerID: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    InsMaturityDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CareCardNo: Mapped[Optional[str]] = mapped_column(String(10))
    CareCardValidPeriod: Mapped[Optional[str]] = mapped_column(String(4))
    CareCardType: Mapped[Optional[str]] = mapped_column(String(4))
    PrescriptionLensFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    PrescriptionContactFlag: Mapped[Optional[bool]] = mapped_column(Boolean)


class CustomerPresContact(Base):
    __tablename__ = 'CustomerPresContact'
    __table_args__ = (
        PrimaryKeyConstraint('CustomerID', name='CustomerPresContact_pkey'),
    )

    CustomerID: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    IssuedOn: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    IssuedByDr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightKReadingV: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightKReadingH: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPalp: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightCorn: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    LeftKReadingV: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftKReadingH: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPalp: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftCorn: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    History: Mapped[Optional[str]] = mapped_column(String(56))
    Medical: Mapped[Optional[str]] = mapped_column(String(56))
    Allergy: Mapped[Optional[str]] = mapped_column(String(56))
    Reason: Mapped[Optional[str]] = mapped_column(String(56))
    Evaluation: Mapped[Optional[str]] = mapped_column(String(56))
    Test: Mapped[Optional[str]] = mapped_column(String(56))


class CustomerPresLens(Base):
    __tablename__ = 'CustomerPresLens'
    __table_args__ = (
        PrimaryKeyConstraint('CustomerID', name='CustomerPresLens_pkey'),
    )

    CustomerID: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    IssuedOn: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    IssuedByDr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightPdDist: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPdNear: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPrism: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightAdd: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    LeftPdDist: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPdNear: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPrism: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftAdd: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))


class Department(Base):
    __tablename__ = 'Department'
    __table_args__ = (
        PrimaryKeyConstraint('DepartmentCode', name='Department_pkey'),
        Index('Department_DepartmentName', 'DepartmentName')
    )

    DepartmentCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    DepartmentName: Mapped[Optional[str]] = mapped_column(String(30))
    SummaryFlag: Mapped[Optional[bool]] = mapped_column(Boolean)


class DeptSummary(Base):
    __tablename__ = 'DeptSummary'
    __table_args__ = (
        PrimaryKeyConstraint('DepartmentCode', 'Year', 'Month', 'FirstDateOfMonth', name='DeptSummary_pkey'),
        Index('DeptSummary_DepartmentCode', 'DepartmentCode'),
        Index('DeptSummary_FirstDateOfMonth', 'FirstDateOfMonth'),
        Index('DeptSummary_Month', 'Month'),
        Index('DeptSummary_Year', 'Year')
    )

    DepartmentCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    Year: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    Month: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    FirstDateOfMonth: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    QtyBF: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtBF: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyCD: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtCD: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtySold: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    AmtCostOfGoodsSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyPurchased: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustedIncr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustedIncr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjustedDecr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjustedDecr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRejected: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRejected: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRestocked: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRestocked: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferIn: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferIn: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferOut: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferOut: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class Doctor(Base):
    __tablename__ = 'Doctor'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='Doctor_pkey'),
        Index('Doctor_DoctorName', 'DoctorName'),
        Index('Doctor_ID', 'ID'),
        Index('Doctor_PostalCode', 'PostalCode')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    DoctorName: Mapped[Optional[str]] = mapped_column(String(40))
    Address: Mapped[Optional[str]] = mapped_column(String(128))
    City_: Mapped[Optional[int]] = mapped_column('City', Integer, server_default=text('0'))
    Province: Mapped[Optional[str]] = mapped_column(String(2))
    Country_: Mapped[Optional[str]] = mapped_column('Country', String(3))
    Phone: Mapped[Optional[str]] = mapped_column(String(10))
    PostalCode: Mapped[Optional[str]] = mapped_column(String(7))
    Fax: Mapped[Optional[str]] = mapped_column(String(10))
    Emergency: Mapped[Optional[str]] = mapped_column(String(15))


class Footer(Base):
    __tablename__ = 'Footer'
    __table_args__ = (
        PrimaryKeyConstraint('FooterCode', name='Footer_pkey'),
    )

    FooterCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    FooterDescription: Mapped[Optional[str]] = mapped_column(String(56))
    FooterNote: Mapped[Optional[str]] = mapped_column(Text)


class Hardening(Base):
    __tablename__ = 'Hardening'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='Hardening_pkey'),
        Index('Hardening_ID', 'ID')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(30))


class Inventory(Base):
    __tablename__ = 'Inventory'
    __table_args__ = (
        PrimaryKeyConstraint('SKU', name='Inventory_pkey'),
        Index('Inventory_AddCode', 'AddCode'),
        Index('Inventory_BaseCurve', 'BaseCurve'),
        Index('Inventory_BrandCode', 'BrandCode'),
        Index('Inventory_Color', 'Color'),
        Index('Inventory_Cylinder', 'Cylinder'),
        Index('Inventory_DeptClassCat', 'DepartmentCode', 'ClassCode', 'CategoryCode'),
        Index('Inventory_Diameter', 'Diameter'),
        Index('Inventory_MaterialCode', 'MaterialCode'),
        Index('Inventory_Model', 'Model'),
        Index('Inventory_Size', 'Size'),
        Index('Inventory_Sphere', 'Sphere'),
        Index('Inventory_SupplierCode', 'SupplierCode')
    )

    DepartmentCode: Mapped[str] = mapped_column(String(2))
    ClassCode: Mapped[str] = mapped_column(String(2))
    CategoryCode: Mapped[str] = mapped_column(String(2))
    SupplierCode: Mapped[str] = mapped_column(String(4))
    BrandCode: Mapped[str] = mapped_column(String(4))
    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    Model: Mapped[Optional[str]] = mapped_column(String(30))
    Color: Mapped[Optional[str]] = mapped_column(String(8))
    Size: Mapped[Optional[str]] = mapped_column(String(6))
    Bridge: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    Temple: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AddCode: Mapped[Optional[str]] = mapped_column(String(2))
    MaterialCode: Mapped[Optional[str]] = mapped_column(String(2))
    Sphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    Cylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    Axis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    BaseCurve: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    Diameter: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    Name: Mapped[Optional[str]] = mapped_column(String(40))
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Remarks: Mapped[Optional[str]] = mapped_column(Text)
    ABCGrading: Mapped[Optional[str]] = mapped_column(String(1))
    InventoryType: Mapped[Optional[str]] = mapped_column(String(1))
    InventoryStatus: Mapped[Optional[str]] = mapped_column(String(1))
    KitSetFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    AverageCost: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    ReOrderLevel: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    ReOrderQty: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    QtyTotalOnHand: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    QtySaleOrder: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    QtyPurchaseOrder: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    QtyHolded: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    QtyInTransit: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    DateLastIssued: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DateLastReceived: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    RetailPriceFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    WholeSalePriceFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    InventoryLotFlag: Mapped[Optional[bool]] = mapped_column(Boolean)


class InvtLotRecord(Base):
    __tablename__ = 'InvtLotRecord'
    __table_args__ = (
        PrimaryKeyConstraint('SKU', 'LotNo', name='InvtLotRecord_pkey'),
        Index('InvtLotRecord_DateReceived', 'DateReceived'),
        Index('InvtLotRecord_LotNo', 'LotNo'),
        Index('InvtLotRecord_SKU', 'SKU'),
        Index('InvtLotRecord_SupplierCode', 'SupplierCode'),
        Index('InvtLotRecord_SupplierDateLotNo', 'SupplierCode', 'DateReceived', 'LotNo')
    )

    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    LotNo: Mapped[str] = mapped_column(String(10), primary_key=True)
    SupplierCode: Mapped[str] = mapped_column(String(4))
    DateReceived: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    QtyPurchased: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    QtyUsed: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    QtyOnHand: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    UnitAmountPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TotalAmountPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class InvtMethod(Base):
    __tablename__ = 'InvtMethod'
    __table_args__ = (
        PrimaryKeyConstraint('InvtMethodCode', name='InvtMethod_pkey'),
        UniqueConstraint('InvtMethodName', name='InvtMethod_InvtMethodName_key')
    )

    InvtMethodCode: Mapped[str] = mapped_column(String(1), primary_key=True)
    InvtMethodName: Mapped[str] = mapped_column(String(15))


class InvtSTDetails(Base):
    __tablename__ = 'InvtSTDetails'
    __table_args__ = (
        PrimaryKeyConstraint('HeaderID', 'SKU', name='InvtSTDetails_pkey'),
        Index('InvtSTDetails_HeaderID', 'HeaderID'),
        Index('InvtSTDetails_ID', 'ID'),
        Index('InvtSTDetails_SKU', 'SKU')
    )

    ID: Mapped[int] = mapped_column(Integer)
    HeaderID: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    ComputerQty: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    PhysicalQty: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    DiffQty: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    AverageCost: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class InvtSTHeader(Base):
    __tablename__ = 'InvtSTHeader'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='InvtSTHeader_pkey'),
        UniqueConstraint('Name', name='InvtSTHeader_Name_key'),
        Index('InvtSTHeader_ID', 'ID')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(30))
    DateOfCreation: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DateOfUpdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DateOfPurge: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Status: Mapped[Optional[int]] = mapped_column(SmallInteger, server_default=text('0'))


class InvtSTImport(Base):
    __tablename__ = 'InvtSTImport'
    __table_args__ = (
        PrimaryKeyConstraint('HeaderID', 'SKU', name='InvtSTImport_pkey'),
        Index('InvtSTImport_HeaderID', 'HeaderID'),
        Index('InvtSTImport_SKU', 'SKU'),
        Index('InvtSTImport_Status', 'Status')
    )

    HeaderID: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    Qty: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    Status: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class InvtSTStatus(Base):
    __tablename__ = 'InvtSTStatus'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='InvtSTStatus_pkey'),
    )

    Code: Mapped[int] = mapped_column(SmallInteger, primary_key=True, server_default=text('0'))
    Name: Mapped[str] = mapped_column(String(10))


class InvtSummary(Base):
    __tablename__ = 'InvtSummary'
    __table_args__ = (
        PrimaryKeyConstraint('SKU', 'Year', 'Month', 'FirstDateOfMonth', name='InvtSummary_pkey'),
        Index('InvtSummary_FirstDateOfMonth', 'FirstDateOfMonth'),
        Index('InvtSummary_Month', 'Month'),
        Index('InvtSummary_SKU', 'SKU'),
        Index('InvtSummary_Year', 'Year')
    )

    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    Year: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    Month: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    FirstDateOfMonth: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    QtyBF: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtBF: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyCD: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtCD: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtySold: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    AmtCostOfGoodsSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyPurchased: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjIncr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjIncr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyAdjDecr: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtAdjDecr: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRejected: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRejected: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRestocked: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRestocked: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferIn: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferIn: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyTransferOut: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtTransferOut: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class JobNature(Base):
    __tablename__ = 'JobNature'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='JobNature_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(1), primary_key=True)
    Name: Mapped[str] = mapped_column(String(20))


class JobStatus(Base):
    __tablename__ = 'JobStatus'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='JobStatus_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(1), primary_key=True)
    Name: Mapped[str] = mapped_column(String(20))


class JobTitle(Base):
    __tablename__ = 'JobTitle'
    __table_args__ = (
        PrimaryKeyConstraint('JobTitleCode', name='JobTitle_pkey'),
        UniqueConstraint('JobTitle', name='JobTitle_JobTitle_key')
    )

    JobTitleCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    JobTitle: Mapped[str] = mapped_column(String(30))


class MaritalStatus(Base):
    __tablename__ = 'MaritalStatus'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='MaritalStatus_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(1), primary_key=True)
    MaritalStatus: Mapped[str] = mapped_column(String(15))


class Material(Base):
    __tablename__ = 'Material'
    __table_args__ = (
        PrimaryKeyConstraint('MaterialCode', name='Material_pkey'),
        Index('Material_MaterialDescription', 'MaterialDescription')
    )

    MaterialCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    MaterialDescription: Mapped[Optional[str]] = mapped_column(String(40))


t_Paste_Errors = Table(
    'Paste Errors', Base.metadata,
    Column('Field0', Text)
)


class PayPer(Base):
    __tablename__ = 'PayPer'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='PayPer_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(1), primary_key=True)
    Name: Mapped[str] = mapped_column(String(10))


class PayPeriod(Base):
    __tablename__ = 'PayPeriod'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='PayPeriod_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(1), primary_key=True)
    Name: Mapped[str] = mapped_column(String(10))


class PaymentMethods(Base):
    __tablename__ = 'PaymentMethods'
    __table_args__ = (
        PrimaryKeyConstraint('PaymentCode', name='PaymentMethods_pkey'),
        UniqueConstraint('PaymentNameLong', name='PaymentMethods_PaymentNameLong_key'),
        UniqueConstraint('PaymentNameShort', name='PaymentMethods_PaymentNameShort_key')
    )

    PaymentCode: Mapped[str] = mapped_column(String(1), primary_key=True)
    PaymentNameShort: Mapped[str] = mapped_column(String(3))
    PaymentNameLong: Mapped[str] = mapped_column(String(20))
    ExchangeRate: Mapped[float] = mapped_column(Double(53), server_default=text('0'))
    RevisedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    TodayAmtOpening: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TodayAmtClosing: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TodayAmtSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TodayNumberOfSold: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    TodayAmtRefund: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TodayNumberOfRefund: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    TodayAmtChanged: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TodayNumberOfChange: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    TodayAmtPaidOut: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TodayNumberOfPaidOut: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    TodayAmtBankIn: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TodayNumberOfBankIn: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AlertLevel: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class PaymentSummary(Base):
    __tablename__ = 'PaymentSummary'
    __table_args__ = (
        PrimaryKeyConstraint('PaymentCode', 'Date', name='PaymentSummary_pkey'),
        Index('PaymentSummary_Date', 'Date'),
        Index('PaymentSummary_NumberOfBankIn', 'NumberOfBankIn'),
        Index('PaymentSummary_NumberOfChange', 'NumberOfChange'),
        Index('PaymentSummary_NumberOfPaidOut', 'NumberOfPaidOut'),
        Index('PaymentSummary_NumberOfRefund', 'NumberOfRefund'),
        Index('PaymentSummary_NumberOfSold', 'NumberOfSold'),
        Index('PaymentSummary_PaymentCode', 'PaymentCode')
    )

    PaymentCode: Mapped[str] = mapped_column(String(1), primary_key=True)
    Date: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    ExchangeRate: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    AmtOpening: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    AmtClosing: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    AmtSold: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    NumberOfSold: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRefund: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    NumberOfRefund: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtChanged: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    NumberOfChange: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtPaidOut: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    NumberOfPaidOut: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtBankIn: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    NumberOfBankIn: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class PrefTxNumber(Base):
    __tablename__ = 'PrefTxNumber'
    __table_args__ = (
        PrimaryKeyConstraint('TxPrefix', name='PrefTxNumber_pkey'),
    )

    TxPrefix: Mapped[str] = mapped_column(String(2), primary_key=True)
    TxNextNumber: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    Description: Mapped[str] = mapped_column(String(30))
    Value: Mapped[Optional[str]] = mapped_column(String(3))
    Remarks: Mapped[Optional[str]] = mapped_column(String(30))


class Preference(Base):
    __tablename__ = 'Preference'
    __table_args__ = (
        PrimaryKeyConstraint('Serial Number', name='Preference_pkey'),
        Index('Preference_CountryCode', 'CountryCode'),
        Index('Preference_NumberOfUser', 'NumberOfUser'),
        Index('Preference_OwnerPostalCode', 'OwnerPostalCode'),
        Index('Preference_UserPostalCode', 'UserPostalCode')
    )

    Serial_Number: Mapped[str] = mapped_column('Serial Number', String(10), primary_key=True)
    NumberOfUser: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    Paltform: Mapped[str] = mapped_column(String(20))
    ProductName: Mapped[str] = mapped_column(String(128))
    UserName: Mapped[str] = mapped_column(String(40))
    OwnerName: Mapped[str] = mapped_column(String(40))
    BranchNumber: Mapped[str] = mapped_column(String(4))
    PSTNumber: Mapped[str] = mapped_column(String(10))
    GSTNumber: Mapped[str] = mapped_column(String(10))
    NextInvtControlNumber: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    NextInvtSKU: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    NextInvoiceNumber: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    NextSalesOrderNumber: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    DateOfInstallation: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UserAddress: Mapped[Optional[str]] = mapped_column(String(128))
    UserCity: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    UserProvince: Mapped[Optional[str]] = mapped_column(String(2))
    UserPostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    UserCountry: Mapped[Optional[str]] = mapped_column(String(20))
    UserPhone: Mapped[Optional[str]] = mapped_column(String(15))
    UserFax: Mapped[Optional[str]] = mapped_column(String(15))
    UserContactPerson: Mapped[Optional[str]] = mapped_column(String(30))
    OwnerAddress: Mapped[Optional[str]] = mapped_column(String(128))
    OwnerCity: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    OwnerProvince: Mapped[Optional[str]] = mapped_column(String(2))
    OwnerPostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    OwnerCountry: Mapped[Optional[str]] = mapped_column(String(20))
    OwnerPhone: Mapped[Optional[str]] = mapped_column(String(15))
    OwnerFax: Mapped[Optional[str]] = mapped_column(String(15))
    OwnerContactPerson: Mapped[Optional[str]] = mapped_column(String(30))
    CountryCode: Mapped[Optional[str]] = mapped_column(String(2))
    TaxARate: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    TaxBRate: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    FiscalPeriod: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CurrentMonth: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Province(Base):
    __tablename__ = 'Province'
    __table_args__ = (
        PrimaryKeyConstraint('ProvinceCode', name='Province_pkey'),
        Index('Province_ProvinceCode', 'ProvinceCode')
    )

    ProvinceName: Mapped[str] = mapped_column(String(26))
    ProvinceCode: Mapped[str] = mapped_column(String(2), primary_key=True)


class ReBuildCost(Base):
    __tablename__ = 'ReBuildCost'
    __table_args__ = (
        PrimaryKeyConstraint('SKU', name='ReBuildCost_pkey'),
    )

    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    AverageCost: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    LSP: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class Remarks(Base):
    __tablename__ = 'Remarks'
    __table_args__ = (
        PrimaryKeyConstraint('RemarksCode', name='Remarks_pkey'),
    )

    RemarksCode: Mapped[str] = mapped_column(String(2), primary_key=True)
    RemarksDescription: Mapped[Optional[str]] = mapped_column(String(56))
    RemarksNote: Mapped[Optional[str]] = mapped_column(Text)


class RetailPrice(Base):
    __tablename__ = 'RetailPrice'
    __table_args__ = (
        PrimaryKeyConstraint('SKU', name='RetailPrice_pkey'),
    )

    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    LeastSellingPrice: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    RetailPrice: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    RetailMarkDownAmt: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    RetailmarkDownPct: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))


class SalesOrderStatus(Base):
    __tablename__ = 'SalesOrderStatus'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='SalesOrderStatus_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(1), primary_key=True)
    Name: Mapped[str] = mapped_column(String(20))


class Salutation(Base):
    __tablename__ = 'Salutation'
    __table_args__ = (
        PrimaryKeyConstraint('Salutation', name='Salutation_pkey'),
    )

    Salutation: Mapped[str] = mapped_column(String(6), primary_key=True)


class Security(Base):
    __tablename__ = 'Security'
    __table_args__ = (
        PrimaryKeyConstraint('LeveL', name='Security_pkey'),
    )

    LeveL: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    Point_of_Sale: Mapped[Optional[bool]] = mapped_column(Boolean)
    Inventory_Control: Mapped[Optional[bool]] = mapped_column(Boolean)
    OLAP: Mapped[Optional[bool]] = mapped_column(Boolean)
    Information_Centre: Mapped[Optional[bool]] = mapped_column(Boolean)
    Coding: Mapped[Optional[bool]] = mapped_column(Boolean)
    Report_Centre: Mapped[Optional[bool]] = mapped_column(Boolean)
    Preference_: Mapped[Optional[bool]] = mapped_column('Preference', Boolean)
    Cost: Mapped[Optional[bool]] = mapped_column(Boolean)


class Sex(Base):
    __tablename__ = 'Sex'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='Sex_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(1), primary_key=True)
    Sex: Mapped[str] = mapped_column(String(10))


class Staff(Base):
    __tablename__ = 'Staff'
    __table_args__ = (
        PrimaryKeyConstraint('StaffCode', name='Staff_pkey'),
        Index('Staff_HomePostalCode', 'HomePostalCode'),
        Index('Staff_StaffFirstName', 'StaffFirstName'),
        Index('Staff_StaffFullName', 'StaffFullName'),
        Index('Staff_StaffLastName', 'StaffLastName')
    )

    StaffCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    SecurityLevel: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    DateHired: Mapped[datetime.datetime] = mapped_column(DateTime)
    SIN: Mapped[str] = mapped_column(String(9))
    StaffFirstName: Mapped[Optional[str]] = mapped_column(String(20))
    StaffLastName: Mapped[Optional[str]] = mapped_column(String(20))
    StaffFullName: Mapped[Optional[str]] = mapped_column(String(40))
    StaffInitial: Mapped[Optional[str]] = mapped_column(String(2))
    JobTitle_: Mapped[Optional[str]] = mapped_column('JobTitle', String(4))
    JobStatus_: Mapped[Optional[str]] = mapped_column('JobStatus', String(1))
    JobNature_: Mapped[Optional[str]] = mapped_column('JobNature', String(1))
    Password: Mapped[Optional[str]] = mapped_column(String(10))
    DateLeaved: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Birthday: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Sex_: Mapped[Optional[str]] = mapped_column('Sex', String(1))
    MaritalStatus_: Mapped[Optional[str]] = mapped_column('MaritalStatus', String(1))
    HomeAddress: Mapped[Optional[str]] = mapped_column(String(128))
    HomeCity: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    HomeProvince: Mapped[Optional[str]] = mapped_column(String(2))
    HomeCountry: Mapped[Optional[str]] = mapped_column(String(3))
    HomePostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    HomePhone: Mapped[Optional[str]] = mapped_column(String(10))
    HomeFax: Mapped[Optional[str]] = mapped_column(String(10))
    SalaryBasic: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    SalaryPer: Mapped[Optional[str]] = mapped_column(String(1))
    SalaryPayPeriod: Mapped[Optional[str]] = mapped_column(String(1))
    BankAccount: Mapped[Optional[str]] = mapped_column(String(15))
    CommissionRate: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    CommissionBonus: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    CommissionGeneral: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class StaffHistory(Base):
    __tablename__ = 'StaffHistory'
    __table_args__ = (
        PrimaryKeyConstraint('StaffCode', 'Date', name='StaffHistory_pkey'),
        Index('StaffHistory_Date', 'Date'),
        Index('StaffHistory_StaffCode', 'StaffCode')
    )

    StaffCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    Date: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    Remarks_: Mapped[str] = mapped_column('Remarks', Text)
    Reason: Mapped[Optional[str]] = mapped_column(String(20))


class Supplier(Base):
    __tablename__ = 'Supplier'
    __table_args__ = (
        PrimaryKeyConstraint('SupplierCode', name='Supplier_pkey'),
        Index('Supplier_SupAccountNo', 'AccountNo'),
        Index('Supplier_SupPostCode', 'PostCode'),
        Index('Supplier_SupplierName', 'SupplierName')
    )

    SupplierCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    SupplierName: Mapped[Optional[str]] = mapped_column(String(50))
    Address: Mapped[Optional[str]] = mapped_column(String(128))
    City_: Mapped[Optional[int]] = mapped_column('City', Integer, server_default=text('0'))
    Province_: Mapped[Optional[str]] = mapped_column('Province', String(2))
    PostCode: Mapped[Optional[str]] = mapped_column(String(8))
    Country_: Mapped[Optional[str]] = mapped_column('Country', String(3))
    PhoneGenVoice: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneGenFax: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneACDeptExt: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneACDeptFax: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneSaleExt: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneSaleFax: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneServiceExt: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneServiceFax: Mapped[Optional[str]] = mapped_column(String(12))
    AccountNo: Mapped[Optional[str]] = mapped_column(String(8))
    DateStarted: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreditLimit: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    PaymentTerms: Mapped[Optional[str]] = mapped_column(String(10))
    ContactPerson: Mapped[Optional[str]] = mapped_column(String(40))
    ContactPersonFlag: Mapped[Optional[str]] = mapped_column(String(1))
    SummaryFlag: Mapped[Optional[str]] = mapped_column(String(1))
    BranchFlag: Mapped[Optional[str]] = mapped_column(String(1))
    Remarks_: Mapped[Optional[str]] = mapped_column('Remarks', Text)
    GSTNumber: Mapped[Optional[str]] = mapped_column(String(10))
    PSTNumber: Mapped[Optional[str]] = mapped_column(String(10))
    TollFreePhone1: Mapped[Optional[str]] = mapped_column(String(24))
    TollFreePhone2: Mapped[Optional[str]] = mapped_column(String(24))
    TollFreeFax1: Mapped[Optional[str]] = mapped_column(String(24))
    TollFreeFax2: Mapped[Optional[str]] = mapped_column(String(24))


class SupplierContactPerson(Base):
    __tablename__ = 'SupplierContactPerson'
    __table_args__ = (
        PrimaryKeyConstraint('SupCode', 'FirstName', 'Initial', 'LastName', name='SupplierContactPerson_pkey'),
        Index('SupplierContactPerson_FirstName', 'FirstName'),
        Index('SupplierContactPerson_Full Name', 'FullName'),
        Index('SupplierContactPerson_Initial', 'Initial'),
        Index('SupplierContactPerson_JobTitle', 'JobTitle'),
        Index('SupplierContactPerson_LastName', 'LastName'),
        Index('SupplierContactPerson_PhoneGeneralFax', 'PhoneGeneralFax'),
        Index('SupplierContactPerson_PhoneGeneralVoice', 'PhoneGeneralVoice'),
        Index('SupplierContactPerson_PhoneHome', 'PhoneHome'),
        Index('SupplierContactPerson_PhoneMobile', 'PhoneMobile'),
        Index('SupplierContactPerson_SupCode', 'SupCode')
    )

    SupCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    FirstName: Mapped[str] = mapped_column(String(20), primary_key=True)
    Initial: Mapped[str] = mapped_column(String(2), primary_key=True)
    LastName: Mapped[str] = mapped_column(String(20), primary_key=True)
    FullName: Mapped[Optional[str]] = mapped_column(String(40))
    Salutation_: Mapped[Optional[str]] = mapped_column('Salutation', String(4))
    JobTitle_: Mapped[Optional[str]] = mapped_column('JobTitle', String(30))
    PhoneGeneralVoice: Mapped[Optional[str]] = mapped_column(String(15))
    PhoneGeneralFax: Mapped[Optional[str]] = mapped_column(String(15))
    PhoneHome: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneMobile: Mapped[Optional[str]] = mapped_column(String(12))
    PhonePager: Mapped[Optional[str]] = mapped_column(String(12))
    PhoneWork: Mapped[Optional[str]] = mapped_column(String(16))


class SupplierSummary(Base):
    __tablename__ = 'SupplierSummary'
    __table_args__ = (
        PrimaryKeyConstraint('SupplierCode', 'Year', 'Month', 'FirstDateOfMonth', name='SupplierSummary_pkey'),
        Index('SupplierSummary_Month', 'Month'),
        Index('SupplierSummary_SupplierCode', 'SupplierCode'),
        Index('SupplierSummary_Year', 'Year')
    )

    SupplierCode: Mapped[str] = mapped_column(String(4), primary_key=True)
    Year: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    Month: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    FirstDateOfMonth: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    QtyPurchased: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtPurchased: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    QtyRejected: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    AmtRejected: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


t_TaxMethod = Table(
    'TaxMethod', Base.metadata,
    Column('TaxCode', String(1), nullable=False),
    Column('TaxName', String(20), nullable=False),
    Index('TaxMethod_TaxCode', 'TaxCode')
)


class TxDetails(Base):
    __tablename__ = 'TxDetails'
    __table_args__ = (
        PrimaryKeyConstraint('TxType', 'TxNumber', 'DateofEntry', 'RowNo', name='TxDetails_pkey'),
        Index('TxDetails_ControlNumber', 'ControlNumber'),
        Index('TxDetails_DateofEntry', 'DateofEntry'),
        Index('TxDetails_RowNo', 'RowNo'),
        Index('TxDetails_SKU', 'SKU'),
        Index('TxDetails_TaxCode', 'TaxCode'),
        Index('TxDetails_TxNumber', 'TxNumber'),
        Index('TxDetails_TxType', 'TxType')
    )

    ControlNumber: Mapped[str] = mapped_column(String(10))
    TxType: Mapped[str] = mapped_column(String(2), primary_key=True)
    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    DateofEntry: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    RowNo: Mapped[float] = mapped_column(Double(53), primary_key=True, server_default=text('0'))
    SKU: Mapped[str] = mapped_column(String(13))
    Remarks_: Mapped[Optional[str]] = mapped_column('Remarks', Text)
    PrescriptionLensFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    PrescriptionContactFlag: Mapped[Optional[bool]] = mapped_column(Boolean)
    Qty: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    UnitAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    UnitCost: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    UnitLSP: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    MarkDownPercent: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    MarkDownAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    Amount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TaxCode: Mapped[Optional[str]] = mapped_column(String(1))


class TxHeader(Base):
    __tablename__ = 'TxHeader'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', name='TxHeader_pkey'),
        Index('TxHeader_ControlNo', 'ControlNumber'),
        Index('TxHeader_CustomerCode', 'CustomerID'),
        Index('TxHeader_DateOfEntry', 'DateOfEntry'),
        Index('TxHeader_PreviousPaid', 'PreviousPaid'),
        Index('TxHeader_ReferenceNo', 'RefNumber'),
        Index('TxHeader_Status', 'Status'),
        Index('TxHeader_SupplierCode', 'SupplierCode'),
        Index('TxHeader_ThisPaid', 'ThisPaid'),
        Index('TxHeader_TrackingNumber', 'TrackingNumber'),
        Index('TxHeader_TxType', 'TxType')
    )

    ControlNumber: Mapped[str] = mapped_column(String(10))
    TxType: Mapped[str] = mapped_column(String(2))
    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    DateOfEntry: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    DateOfCreation: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    RefNumber: Mapped[Optional[str]] = mapped_column(String(10))
    TrackingNumber: Mapped[Optional[str]] = mapped_column(String(10))
    CustomerID: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    SupplierCode: Mapped[Optional[str]] = mapped_column(String(4))
    SecondDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Particulars: Mapped[Optional[str]] = mapped_column(Text)
    TotalCost: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TotalSale: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TaxA: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TaxB: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TaxC: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    OtherCharges: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    GrossSale: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    SalesDiscount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TotalAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TotalQty: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    PreviousPaid: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    ThisPaid: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    Change: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    PrintCounter: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    PaymentLink: Mapped[Optional[int]] = mapped_column(SmallInteger, server_default=text('0'))
    SalesPersonLink: Mapped[Optional[int]] = mapped_column(SmallInteger, server_default=text('0'))
    Status: Mapped[Optional[str]] = mapped_column(String(1))


class TxPayment(Base):
    __tablename__ = 'TxPayment'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', 'PaymentLineNo', 'Type', name='TxPayment_pkey'),
        Index('TxPayment_AuthorizationCode', 'AuthorizationCode'),
        Index('TxPayment_PaymentSeq#', 'PaymentLineNo'),
        Index('TxPayment_TxNumber', 'TxNumber'),
        Index('TxPayment_Type', 'Type')
    )

    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    PaymentLineNo: Mapped[float] = mapped_column(Double(53), primary_key=True, server_default=text('0'))
    Type: Mapped[str] = mapped_column(String(1), primary_key=True)
    CardNumber: Mapped[Optional[str]] = mapped_column(String(30))
    AuthorizationCode: Mapped[Optional[str]] = mapped_column(String(10))
    AmountTender: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    ExchangeRate: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    EqAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    TotalThisPay: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class TxSOrderAdd(Base):
    __tablename__ = 'TxSOrderAdd'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', 'LineNumber', name='TxSOrderAdd_pkey'),
        Index('TxSOrderAdd_LineNumber', 'LineNumber')
    )

    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    LineNumber: Mapped[float] = mapped_column(Double(53), primary_key=True, server_default=text('0'))
    Supplier_: Mapped[Optional[str]] = mapped_column('Supplier', String(30))
    Brand_: Mapped[Optional[str]] = mapped_column('Brand', String(30))
    Model: Mapped[Optional[str]] = mapped_column(String(30))


class TxSOrderCont(Base):
    __tablename__ = 'TxSOrderCont'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', 'LineNumber', name='TxSOrderCont_pkey'),
        Index('TxSOrderCont_LineNumber', 'LineNumber'),
        Index('TxSOrderCont_TxNumber', 'TxNumber')
    )

    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    LineNumber: Mapped[float] = mapped_column(Double(53), primary_key=True, server_default=text('0'))
    IssuedOn: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    IssuedBy: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightKReadingV: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightKReadingH: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPalp: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightCorn: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    LeftKReadingV: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftKReadingH: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPalp: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftCorn: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    History: Mapped[Optional[str]] = mapped_column(String(56))
    Medical: Mapped[Optional[str]] = mapped_column(String(56))
    Allergy: Mapped[Optional[str]] = mapped_column(String(56))
    Reason: Mapped[Optional[str]] = mapped_column(String(56))
    Evaluation: Mapped[Optional[str]] = mapped_column(String(56))
    Test: Mapped[Optional[str]] = mapped_column(String(56))
    SpecialInstruction: Mapped[Optional[str]] = mapped_column(String(128))


class TxSOrderExtra(Base):
    __tablename__ = 'TxSOrderExtra'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', name='TxSOrderExtra_pkey'),
    )

    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    Redo: Mapped[Optional[bool]] = mapped_column(Boolean)
    Warranty: Mapped[Optional[bool]] = mapped_column(Boolean)
    Mail: Mapped[Optional[bool]] = mapped_column(Boolean)
    Msd: Mapped[Optional[bool]] = mapped_column(Boolean)
    Remarks_: Mapped[Optional[int]] = mapped_column('Remarks', Integer, server_default=text('0'))


class TxSOrderFrame(Base):
    __tablename__ = 'TxSOrderFrame'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', 'LineNumber', name='TxSOrderFrame_pkey'),
        Index('TxSOrderFrame_LineNumber', 'LineNumber')
    )

    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    LineNumber: Mapped[float] = mapped_column(Double(53), primary_key=True, server_default=text('0'))
    Supply: Mapped[Optional[bool]] = mapped_column(Boolean)
    Enclosed: Mapped[Optional[bool]] = mapped_column(Boolean)
    Follow: Mapped[Optional[bool]] = mapped_column(Boolean)
    Lenses: Mapped[Optional[bool]] = mapped_column(Boolean)
    Mode: Mapped[Optional[str]] = mapped_column(String(30))
    Color: Mapped[Optional[str]] = mapped_column(String(8))
    EyeSize: Mapped[Optional[str]] = mapped_column(String(6))
    Bridge: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    Temple: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    R1: Mapped[Optional[str]] = mapped_column(String(10))
    R2: Mapped[Optional[str]] = mapped_column(String(10))
    R3: Mapped[Optional[str]] = mapped_column(String(10))
    A: Mapped[Optional[str]] = mapped_column(String(10))
    B: Mapped[Optional[str]] = mapped_column(String(10))
    SpecialInstruction: Mapped[Optional[str]] = mapped_column(String(128))


class TxSOrderLens(Base):
    __tablename__ = 'TxSOrderLens'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', 'LineNumber', name='TxSOrderLens_pkey'),
        Index('TxSOrderLens_RowNo', 'LineNumber'),
        Index('TxSOrderLens_TxNumber', 'TxNumber')
    )

    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    LineNumber: Mapped[float] = mapped_column(Double(53), primary_key=True, server_default=text('0'))
    IssuedOn: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    IssuedBy: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    RightPdDist: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPdNear: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPrism: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightAdd: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightStyle: Mapped[Optional[str]] = mapped_column(String(30))
    RightSegHt: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RigthOC: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RigthBase: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    RightVD: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftSphere: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftCylinder: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftAxis: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    LeftPdDist: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPdNear: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPrism: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftAdd: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftPupil: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftStyle: Mapped[Optional[str]] = mapped_column(String(30))
    LeftSegHt: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftOC: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftBase: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    LeftVD: Mapped[Optional[float]] = mapped_column(Double(53), server_default=text('0'))
    Type: Mapped[Optional[str]] = mapped_column(String(30))
    Hardening_: Mapped[Optional[str]] = mapped_column('Hardening', String(30))
    Material_: Mapped[Optional[str]] = mapped_column('Material', String(2))
    Coating: Mapped[Optional[str]] = mapped_column(String(2))
    Tint: Mapped[Optional[str]] = mapped_column(String(30))
    Others: Mapped[Optional[str]] = mapped_column(String(30))
    HardCoat: Mapped[Optional[bool]] = mapped_column(Boolean)
    ARCoat: Mapped[Optional[bool]] = mapped_column(Boolean)
    UV: Mapped[Optional[bool]] = mapped_column(Boolean)


class TxSalePerson(Base):
    __tablename__ = 'TxSalePerson'
    __table_args__ = (
        PrimaryKeyConstraint('TxNumber', 'SalesRowNo', 'StaffCode', name='TxSalePerson_pkey'),
        Index('TxSalePerson_SalesSeq#', 'SalesRowNo'),
        Index('TxSalePerson_StaffCode', 'StaffCode'),
        Index('TxSalePerson_TxNumber', 'TxNumber')
    )

    TxNumber: Mapped[str] = mapped_column(String(10), primary_key=True)
    SalesRowNo: Mapped[float] = mapped_column(Double(53), primary_key=True, server_default=text('0'))
    StaffCode: Mapped[str] = mapped_column(String(4), primary_key=True)


class UtilCheckLog(Base):
    __tablename__ = 'UtilCheckLog'
    __table_args__ = (
        PrimaryKeyConstraint('LogNumber', name='UtilCheckLog_pkey'),
        Index('UtilCheckLog_ParentKey', 'ParentKey')
    )

    LogNumber: Mapped[int] = mapped_column(Integer, primary_key=True)
    DateOfLog: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ParentTable: Mapped[Optional[str]] = mapped_column(String(30))
    ParentKey: Mapped[Optional[str]] = mapped_column(String(30))
    Remarks_: Mapped[Optional[str]] = mapped_column('Remarks', String(50))


class WholesalePrice(Base):
    __tablename__ = 'WholesalePrice'
    __table_args__ = (
        PrimaryKeyConstraint('SKU', name='WholesalePrice_pkey'),
    )

    SKU: Mapped[str] = mapped_column(String(13), primary_key=True)
    SuggestedRetailPrice: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    SellingPriceGradeA: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    SellingPriceGradeB: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))
    SellingPriceGradeC: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(19, 4), server_default=text('0'))


class ZDefaultClass(Base):
    __tablename__ = 'Z_DefaultClass'
    __table_args__ = (
        PrimaryKeyConstraint('Code', name='Z_DefaultClass_pkey'),
    )

    Code: Mapped[str] = mapped_column(String(2), primary_key=True)
    Name: Mapped[str] = mapped_column(String(20))


class ZDefaultRemarks(Base):
    __tablename__ = 'Z_DefaultRemarks'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='Z_DefaultRemarks_pkey'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Group: Mapped[int] = mapped_column(SmallInteger, server_default=text('0'))
    Remarks_: Mapped[Optional[str]] = mapped_column('Remarks', String(128))


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pkey'),
        Index('ix_users_email', 'email', unique=True),
        Index('ix_users_id', 'id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[Optional[str]] = mapped_column(String)
    hashed_password: Mapped[Optional[str]] = mapped_column(String)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)
