from distutils.core import setup

setup(
name='Subway', 
version='1.0', # 파일명이 아니라 모듈명을 입력 (.py라는 확장자는 제외)
py_modules=['Subway'], 
packages=['image', 'modules'], 
package_data = {'image': ['*.png'], 'modules': ['*.py']}, )
