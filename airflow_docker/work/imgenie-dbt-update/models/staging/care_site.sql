{{ config(materialized='incremental',
  depends_on=['ref("base_table_organization")']
  ,unique_key='care_site_id'
  ,tags=['care_site']) 
   }}
select 
substring(identifier from '"code": "([^"]+)"') as "care_site_id",
name as "care_site_name",
substring(type from '"code": "([^"]+)"') as "place_of_service_concept_id",
address::json -> 'text'  as "location_id"
,create_time
FROM {{ ref('base_table_organization') }}
{% if is_incremental() %}
where create_time > (select max(create_time) from {{ this }})
{% endif %}
    --並未標示完整只能依文體猜測使用的值