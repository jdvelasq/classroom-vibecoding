from pathlib import Path
import shutil


COURSE_ACTIVITIES = {
    "fundamentos": [
        "common/P001_hola_mundo",
        "descriptiva/P100_mapreduce_word_count",
        "descriptiva/P101_manejo_editor",
        "descriptiva/P102_csv2json",
        "descriptiva/P103_drivers_pandas",
        "descriptiva/P104_drivers_sqlite",
        "descriptiva/P105_drivers_chatgpt",
        "descriptiva/P106_limpieza_pandas",
        "descriptiva/P107_limpieza_sql",
        "descriptiva/P108_anonimizacion_pandas",
        "descriptiva/P109_anonimizacion_sql",
        "predictiva/P200_regresion_basica",
        "predictiva/P201_clasificacion_basica_imagenes",
        "predictiva/P202_tokenizacion",
        "predictiva/P203_clasificacion_basica_texto",
        "predictiva/P204_clasificacion_basica_numerica",
        "predictiva/P205_priorizacion_con_probabilidades",
        "predictiva/P206_clustering_demanda",
        "predictiva/P207_clustering_mercadeo",
        "prescriptiva/P300_encuadre_analitico_de_decisiones",
        "prescriptiva/P301_air_france_447",
        "prescriptiva/P302_politica_desde_evidencia_y_restricciones",
        "productos/P400_code_testing_unittest",
        "productos/P401_code_testing_pytest",
        "productos/P402_data_testing_pytest_pandas",
    ],
    "data": [
        "common/P001_hola_mundo",
        "descriptiva/P100_mapreduce_word_count",
        "data/P500_superstore_metricas",
        "data/P501_superstore_serving",
        "data/P502_superstore_linaje",
        "data/P503_scopus_relacional",
        "data/P504_scopus_sql_basico",
        "data/P505_scopus_sql_intermedio",
        "data/P506_scopus_sql_avanzado",
        "data/P507_scopus_sql_analitico",
        "data/P508_scopus_sqlalchemy",
        "data/P510_datacamp_valoraciones",
        "data/P511_superstore_integracion",
        "data/P512_superstore_warehouse",
        "data/P513_superstore_batch",
        "data/P514_superstore_etl",
        "data/P515_superstore_elt",
        "data/P516_vermont_calidad",
        "data/P517_vermont_contratos",
        "data/P518_github_api",
        "data/P519_mapreduce_operators",
        "data/P520_mapreduce_basico",
        "data/P521_mapreduce_avanzado",
        "data/P522_mapreduce_multiprocessing",
        "data/P523_mapreduce_particionamiento",
        "data/P524_seleccion_formato_datos",
        "data/P525_particionamiento_parquet",
    ],
    "descriptiva": [
        "common/P001_hola_mundo",
        "descriptiva/P100_mapreduce_word_count",
        "descriptiva/P101_manejo_editor",
        "descriptiva/P102_csv2json",
        "descriptiva/P103_drivers_pandas",
        "descriptiva/P104_drivers_sqlite",
        "descriptiva/P105_drivers_chatgpt",
        "descriptiva/P106_limpieza_pandas",
        "descriptiva/P107_limpieza_sql",
        "descriptiva/P108_anonimizacion_pandas",
        "descriptiva/P109_anonimizacion_sql",
        "descriptiva/P120_retail_sales",
        "descriptiva/P121_vuelos",
        "descriptiva/P122_supply_chain",
        "descriptiva/P123_scopus",
        "descriptiva/P124_marketing_dashboard",
        "descriptiva/P125_salarios",
        "descriptiva/P150_ventas_tabla",
        "descriptiva/P151_ventas_mart",
        "descriptiva/P152_ventas_olap",
        "descriptiva/P153_ventas_kpis",
        "descriptiva/P154_ventas_dashboard",
    ],
    "predictiva": [
        "common/P001_hola_mundo",
        "predictiva/P200_regresion_basica",
        "predictiva/P201_clasificacion_basica_imagenes",
        "predictiva/P202_tokenizacion",
        "predictiva/P203_clasificacion_basica_texto",
        "predictiva/P204_clasificacion_basica_numerica",
        "predictiva/P205_priorizacion_con_probabilidades",
        "predictiva/P206_clustering_demanda",
        "predictiva/P207_clustering_mercadeo",
        "predictiva/P208_sir_basico",
        "predictiva/P209_sir_adaptativo",
        "predictiva/P210_pronostico_adopcion_producto",
        "predictiva/P211_pronostico_congestion_servicio",
        "predictiva/P212_tiempo_hasta_abandono",
        "predictiva/P213_transicion_estados_cliente",
        "predictiva/P214_recomendacion_apriori",
        "predictiva/P215_filtrado_colaborativo",
        "predictiva/P216_series_de_tiempo",
        "predictiva/P217_deployment_web_app",
        "predictiva/P218_deployment_api",
        "predictiva/P219_hiperparametros",
        "predictiva/P220_pipelines",
        "predictiva/P221_selection_inputs_regresion",
        "predictiva/P222_selection_inputs_clasificacion",
        "predictiva/P223_lasso",
        "predictiva/P224_reduccion_dimensionalidad",
        "predictiva/P225_estructura_mercado",
    ],
    "prescriptiva": [
        "common/P001_hola_mundo",
        "prescriptiva/P300_encuadre_analitico_de_decisiones",
        "prescriptiva/P301_air_france_447",
        "prescriptiva/P302_politica_desde_evidencia_y_restricciones",
        "prescriptiva/P303_politicas_y_supervision_humana",
        "prescriptiva/P304_airline_revenue_management",
        "prescriptiva/P305_tax_inspections",
        "prescriptiva/P306_credit_campaign_targeting",
        "prescriptiva/P307_decision_informada_por_pronosticos",
        "prescriptiva/P308_annie_moore_refugee_resettlement",
        "prescriptiva/P309_covid_hospital_capacity",
        "prescriptiva/P310_monte_carlo_para_politicas",
        "prescriptiva/P311_evaluacion_politicas_por_simulacion",
        "prescriptiva/P312_sensibilidad_y_tradespace",
        "prescriptiva/P313_delivery_fleet_capacity",
        "prescriptiva/P314_storm_response_crews",
        "prescriptiva/P315_wildfire_resource_positioning",
        "prescriptiva/P316_humanitarian_food_aid",
        "prescriptiva/P317_flood_protection_investment",
        "prescriptiva/P318_hydrothermal_planning",
        "prescriptiva/P319_catalog_assortment",
        "prescriptiva/P320_equidad_y_responsabilidad_prescriptiva",
        "prescriptiva/P321_comunicacion_y_seguimiento_politicas",
        "prescriptiva/P322_valor_informacion_y_experimentacion",
    ],
    "productos": [
        "common/P001_hola_mundo",
        "productos/P400_code_testing_unittest",
        "productos/P401_code_testing_pytest",
        "productos/P402_data_testing_pytest_pandas",
        "productos/P403_model_testing_pytest",
        "productos/P404_model_input_testing_pytest",
        "productos/P405_logs",
        "productos/P406_config_cmd_line",
        "productos/P407_config_file",
        "productos/P408_version_control",
        "productos/P409_branch_merge",
        "productos/P410_github_remote",
        "productos/P411_pull_request",
        "productos/P412_repro_environment",
        "productos/P413_makefile",
        "productos/P414_nox",
        "productos/P415_github_actions",
        "productos/P416_github_actions_nox",
        "productos/P417_pipeline_integration_test",
        "productos/P418_container",
        "productos/P419_random_seed",
        "productos/P420_experiment_tracking",
        "productos/P421_model_registry",
        "productos/P422_model_monitoring",
        "productos/P423_model_performance_monitoring",
        "productos/P424_model_rollback",
        "productos/P425_api_contract",
        "productos/P426_api_container",
        "productos/P427_secret_config",
        "productos/P428_schedule",
        "productos/P429_prefect",
        "productos/P430_idempotency",
        "productos/P431_data_versioning",
        "productos/P432_duckdb_transformation",
        "productos/P433_dbt_duckdb",
        "productos/P434_contract_versioning",
        "productos/P435_schema_migration",
        "productos/P436_watermark",
        "productos/P437_late_arriving_data",
        "productos/P438_backfill",
        "productos/P439_data_freshness",
        "productos/P440_data_reconciliation",
        "productos/P441_data_quarantine",
        "productos/P442_data_observability",
        "productos/P443_data_lineage",
        "productos/P444_release_version",
        "productos/P445_service_level",
        "productos/P446_runbook",
        "productos/P447_incident_response",
        "productos/P448_backup_restore",
        "productos/P449_cost_monitoring",
        "productos/P450_human_review",
        "productos/P451_user_feedback",
        "productos/P452_access_control",
        "productos/P453_data_masking",
        "productos/P454_data_catalog",
        "productos/P455_data_retention",
    ],
}

DISTRIBUTION_DIR = Path(__file__).resolve().parent.parent
IMPLEMENTATION_DIR = DISTRIBUTION_DIR.parent / "implementation"


def prepare_course_directories():
    for course_id in COURSE_ACTIVITIES:
        course_dir = DISTRIBUTION_DIR / course_id

        if course_dir.exists():
            shutil.rmtree(course_dir)

        course_dir.mkdir()


def validate_activity_directories():
    missing_directories = []

    for course_id, activity_paths in COURSE_ACTIVITIES.items():
        for activity_path in activity_paths:
            source_dir = IMPLEMENTATION_DIR / activity_path

            if not source_dir.is_dir():
                missing_directories.append(f"{course_id}: {activity_path}")

    if missing_directories:
        missing_text = "\n".join(missing_directories)
        raise FileNotFoundError(f"Activity directories not found:\n{missing_text}")


def copy_activity(source_dir, target_dir):
    shutil.copytree(source_dir, target_dir)


def populate_course_directories():
    for course_id, activity_paths in COURSE_ACTIVITIES.items():
        course_dir = DISTRIBUTION_DIR / course_id

        for activity_path in activity_paths:
            source_dir = IMPLEMENTATION_DIR / activity_path
            target_dir = course_dir / source_dir.name
            copy_activity(source_dir, target_dir)


def main():
    validate_activity_directories()
    prepare_course_directories()
    populate_course_directories()


if __name__ == "__main__":
    main()
