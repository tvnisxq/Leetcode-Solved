SELECT
    eu.Unique_id as Unique_id, e.name as name
FROM
    Employees e left join EmployeeUNI eu on e.id = eu.id