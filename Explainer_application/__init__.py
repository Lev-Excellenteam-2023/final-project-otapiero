import main_app
async def explain_pptx(pptx_file_path: str, folder_result_path: str, file_name: str):
    try:
        await main_app.explain_pptx(pptx_file_path=pptx_file_path, folder_result_path=folder_result_path, file_name=file_name)
    except Exception as e:
        raise e

