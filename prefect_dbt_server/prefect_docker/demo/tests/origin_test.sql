WITH table1_counts AS (
  SELECT
    COUNT(*) AS count1
  FROM
   {{ var('myschema') }}.{{ var('myorigin') }}
)
SELECT
  1
FROM
  table1_counts
where count1 <= 0