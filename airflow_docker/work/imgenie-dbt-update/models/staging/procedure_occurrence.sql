
{{ config(materialized='incremental',
  depends_on=['ref("base_table_procedure")']
  ,unique_key='procedure_occurrence_id'
  ,tags=['procedure_occurrence']) 
   }}

SELECT
'identifier' as "procedure_occurrence_id", --缺漏
'identifier' as "visit_occurrence_id", --缺漏
'identifier' as "person_id", --缺漏
code as "procedure_concept_id",
'performedDateTime' as "procedure_date", --缺漏
'performedDateTime'  as "procedure_datetime", --缺漏
'performer' as "provider_id" --缺漏
,create_time
FROM 
  {{   ref('base_table_procedure')  }}
  
  {% if is_incremental() %}
where  create_time > (select max(create_time) from {{ this  }}  LIMIT 1)
{% endif %}