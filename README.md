- Build documentation
    ```shell
    cd docs
    sphinx-build source build
    ```

- Build binary distribution
    ```shell
    python3 setup.py bdist_wheel 
    ```

- Upload to PyPI
    ```shell
    twine upload dist/*
    ```

- Install from PyPI
    ```shell
    pip install <package_name>
    ```
