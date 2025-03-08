--Example Query 1: Total Patient Visits by Month

SELECT
    t.Year,
    t.Month,
    COUNT(v.VisitID) AS TotalVisits
FROM FactPatientVisits v
JOIN DimTime t ON v.VisitDate = t.Date
GROUP BY t.Year, t.Month
ORDER BY t.Year, t.Month;

##Query 2: Total Payroll Cost by Department

SELECT
    d.DepartmentName,
    SUM(p.GrossPay) AS TotalPayrollCost
FROM FactPayroll p
JOIN DimDepartment d ON p.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;

--BI Tool Connection:

--The BI tool (e.g., Tableau) can be connected via live query connections or through periodic extracts.
--Live connections offer real-time data visibility if performance and data volume allow.
--Extracts can be used to improve performance for complex dashboards.


