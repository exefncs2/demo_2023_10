
  {{ config(materialized='incremental',
  depends_on=['ref("base_table_encounter")']
  ,unique_key='visit_occurence_id'
  ,tags=['visit_occurrence']) 
   }}
SELECT
jsonb_array_elements(identifier::jsonb) ->> 'value' as "visit_occurence_id", --取value
'identifier' as "visit_source_value", --沒有值
-- jsonb_array_elements(location::jsonb) -> location -> managingOrganization ->> identifier as "care_site_id", --Encounter.location.location.managingOrganization.identifier
jsonb_array_elements(location::jsonb) -> 'location' ->> 'display'  as "care_site_id", 
'unknown' as "admitting_from_concept_id", --不明 Encounter.hospitalization.extension : cdmh-pcornet-admitting-source-facility-type
'unknown' as "admitting_from_source_value", --不明 Encounter.hospitalization.extension : cdmh-pcornet-admitting-source-facility-type
'unknown' as "admitting_from_source_concept_id", --不明  Encounter.hospitalization.extension : cdmh-pcornet-admitting-source-facility-type
'unknown' as "discharge_to_concept_id", --不明  cdmh-pcornet-discharge-status
'unknown' as "discharge_to_source_value", --不明  cdmh-pcornet-discharge-status
'partOf' as "preceding_visit_occurence", --缺漏 partOf
'subject.identifier' as "person_id",
-- jsonb_array_elements(subject::jsonb) ->> 'identifier' as "person_id", --缺漏
jsonb_array_elements(type::jsonb) ->> 'id' as "visit_concept_id", -- 缺漏 Encounter.type
jsonb_array_elements(type::jsonb) ->> 'text' as "visit_source_value2", -- 缺漏 Encounter.type
period::jsonb ->> 'start' as "visit_start_date", -- 時間都一樣?
period::jsonb ->> 'start' as "visit_start_datetime", -- 時間都一樣?
period::jsonb ->> 'start' as "visit_end_date", -- 時間都一樣?
period::jsonb ->> 'start' as "visit_end_datetime", -- 時間都一樣?
'unknown' as "visit_type_concept_id", --不明  Encounter.diagnosis.extension : cdmh-pcornet-diagnosis-origin
'unknown' as "visit_type_source_value", --不明  Encounter.diagnosis.extension : cdmh-pcornet-diagnosis-origin
'performer.identifier' as "provider_id"
--jsonb_array_elements(performer::jsonb) ->> 'identifier' as "provider_id" -- 缺漏 performer
,create_time
FROM 
  {{   ref('base_table_encounter')  }}
 {% if is_incremental() %}
where  create_time > (select max(create_time) from {{ this  }}  LIMIT 1)
{% endif %}