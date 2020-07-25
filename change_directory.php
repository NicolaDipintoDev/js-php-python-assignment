<?php

// I believe that clean code doesn't need comments excpet for very complicated algorithms

class Path
{
    public $currentPath = '/';
    public function __construct(string $currentPath)
    {
        $this->currentPath .= $this->removeFirstSlash($currentPath);
    }

    private function removeFirstSlash(string $path)
    {
        return ltrim($path, '/');
    }

    public function cd(string $path = null)
    {
        if (!isset($path)) {
            $this->currentPath = '/';
        } else {
            $this->changecurrentPath(
                $this->pathAsArray(
                    $this->removeFirstSlash($path)
                )
            );
        }
    }

    private function changeCurrentPath(array $pathArray)
    {
        foreach ($pathArray as &$pathPiece) {
            $this->setCurrentPath($pathPiece);
        }
    }

    private function pathAsArray(string $path)
    {
        return explode('/', $path);
    }

    private function setCurrentPath(string $pathPiece)
    {
        if ($pathPiece === '..') {
            if ($this->currentPath !== '/') {
                $this->backToFather();
            }
        } else if ($pathPiece !== '') {
            $this->addChildren($pathPiece);
        }
    }

    private function backToFather()
    {
        $pathArray =
            $this->pathAsArray(
                $this->removeFirstSlash(
                    $this->currentPath
                )
            );
        array_pop($pathArray);

        if (count($pathArray) > 0) {
            $this->currentPath = implode('/', $pathArray);
        } else {
            $this->currentPath = '/';
        }
    }

    private function addChildren(string $children)
    {
        if ($this->currentPath !== '/') {
            $this->currentPath .= '/';
        }
        $this->currentPath .= $children;
    }
}

$path = new Path('/a/b/c/d');
$path->cd('../x');
echo $path->currentPath;
